#!/usr/bin/env python3
import ast
from dataclasses import dataclass, asdict

MAX_DIFFICULTY_SCORE = 10.0
LOWER_BOUND = 0.30
UPPER_BOUND = 0.70


@dataclass
class DifficultyMetrics:
    lines_of_code: int
    num_inputs: int
    nesting_depth: int
    decision_paths: int
    function_calls: int
    state_changes: int
    structure_score: float
    difficulty_score: float
    difficulty_pct: float
    difficulty_bucket: str
    kept: bool


class CodeComplexityAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.current_function = None
        self.metrics = {}
        self._nesting = 0
        self._max_nesting = 0

    def visit_FunctionDef(self, node):
        old_function    = self.current_function
        old_nesting     = self._nesting
        old_max_nesting = self._max_nesting

        self.current_function = node.name
        self._nesting = 0
        self._max_nesting = 0

        num_inputs = len(node.args.args) + len(node.args.kwonlyargs)
        if node.args.vararg:
            num_inputs += 1
        if node.args.kwarg:
            num_inputs += 1

        lines_of_code = (
            node.end_lineno - node.lineno + 1
            if hasattr(node, "end_lineno") and node.end_lineno is not None
            else 0
        )

        self.metrics[node.name] = {
            "lines_of_code": lines_of_code,
            "num_inputs": num_inputs,
            "nesting_depth": 0,
            "decision_paths": 1,
            "function_calls": 0,
            "state_changes": 0,
        }

        self.generic_visit(node)
        self.metrics[node.name]["nesting_depth"] = self._max_nesting

        self.current_function = old_function
        self._nesting         = old_nesting
        self._max_nesting     = old_max_nesting

    def _enter_nested_block(self):
        self._nesting += 1
        self._max_nesting = max(self._max_nesting, self._nesting)

    def _exit_nested_block(self):
        self._nesting -= 1

    def visit_If(self, node):
        if self.current_function:
            self.metrics[self.current_function]["decision_paths"] += 1
        self._enter_nested_block()
        self.generic_visit(node)
        self._exit_nested_block()

    def visit_For(self, node):
        if self.current_function:
            self.metrics[self.current_function]["decision_paths"] += 1
        self._enter_nested_block()
        self.generic_visit(node)
        self._exit_nested_block()

    def visit_While(self, node):
        if self.current_function:
            self.metrics[self.current_function]["decision_paths"] += 1
        self._enter_nested_block()
        self.generic_visit(node)
        self._exit_nested_block()

    def visit_Try(self, node):
        if self.current_function:
            self.metrics[self.current_function]["decision_paths"] += max(1, len(node.handlers))
        self._enter_nested_block()
        self.generic_visit(node)
        self._exit_nested_block()

    def visit_BoolOp(self, node):
        if self.current_function:
            self.metrics[self.current_function]["decision_paths"] += max(0, len(node.values) - 1)
        self.generic_visit(node)

    def visit_IfExp(self, node):
        if self.current_function:
            self.metrics[self.current_function]["decision_paths"] += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        if self.current_function:
            self.metrics[self.current_function]["function_calls"] += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        if self.current_function:
            self.metrics[self.current_function]["state_changes"] += len(node.targets)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        if self.current_function:
            self.metrics[self.current_function]["state_changes"] += 1
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        if self.current_function:
            self.metrics[self.current_function]["state_changes"] += 1
        self.generic_visit(node)


def _normalize(value, low, high):
    if high == low:
        return 0.0
    return max(0.0, min(1.0, (value - low) / (high - low)))


def _bucket(score):
    if score < 3:
        return "Easy"
    if score < 6:
        return "Moderate"
    if score < 8:
        return "Hard"
    return "Very Hard"


def _score_metrics(m: dict) -> tuple[float, float, float]:
    loc_score       = _normalize(m["lines_of_code"], 1, 10) * 10
    inputs_score    = _normalize(m["num_inputs"],    1,  3) * 10
    nesting_score   = _normalize(m["nesting_depth"], 0,  3) * 10
    structure_score = (loc_score + inputs_score + nesting_score) / 3

    decision_score = _normalize(m["decision_paths"], 1, 6) * 10
    call_score     = _normalize(m["function_calls"], 0, 5) * 10
    state_score    = _normalize(m["state_changes"],  0, 4) * 10

    difficulty_score = (
        0.25 * structure_score +
        0.40 * decision_score  +
        0.25 * call_score      +
        0.10 * state_score
    )

    difficulty_pct = difficulty_score / MAX_DIFFICULTY_SCORE
    return round(structure_score, 2), round(difficulty_score, 2), round(difficulty_pct, 4)


def analyse_variant(code: str) -> dict[str, DifficultyMetrics]:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {}

    analyzer = CodeComplexityAnalyzer()
    analyzer.visit(tree)

    results = {}
    for fn_name, m in analyzer.metrics.items():
        structure_score, difficulty_score, difficulty_pct = _score_metrics(m)
        kept = LOWER_BOUND <= difficulty_pct <= UPPER_BOUND

        results[fn_name] = DifficultyMetrics(
            lines_of_code    = m["lines_of_code"],
            num_inputs       = m["num_inputs"],
            nesting_depth    = m["nesting_depth"],
            decision_paths   = m["decision_paths"],
            function_calls   = m["function_calls"],
            state_changes    = m["state_changes"],
            structure_score  = structure_score,
            difficulty_score = difficulty_score,
            difficulty_pct   = difficulty_pct,
            difficulty_bucket= _bucket(difficulty_score),
            kept             = kept,
        )
    return results


def filter_variants(variants: list[dict], original_score: float = None) -> dict:
    kept      = []
    discarded = []

    for variant in variants:
        code    = variant.get("prompt", "")
        metrics = analyse_variant(code)

        if not metrics:
            discarded.append({**variant, "metrics": None, "reason": "syntax error"})
            continue

        fn_name, m = next(iter(metrics.items()))
        m_dict     = asdict(m)

        # score relative to the original problem if available, otherwise absolute
        if original_score and original_score > 0:
            relative_pct = m.difficulty_score / original_score
        else:
            relative_pct = m.difficulty_pct

        pct_label = f"{relative_pct * 100:.1f}%"
        kept_flag = LOWER_BOUND <= relative_pct <= UPPER_BOUND

        if kept_flag:
            kept.append({**variant, "fn_name": fn_name, "metrics": m_dict, "relative_pct": relative_pct})
        else:
            reason = (
                f"too easy ({pct_label} < {int(LOWER_BOUND*100)}%)"
                if relative_pct < LOWER_BOUND
                else f"too hard ({pct_label} > {int(UPPER_BOUND*100)}%)"
            )
            discarded.append({**variant, "fn_name": fn_name, "metrics": m_dict, "relative_pct": relative_pct, "reason": reason})

    return {"kept": kept, "discarded": discarded}


def filter_variant_tree(tree: dict) -> dict:
    filtered_tree = {}

    # score the original hard problem first
    original_score = None
    if tree.get("hard"):
        hard_code = tree["hard"][0].get("prompt", "")
        hard_metrics = analyse_variant(hard_code)
        if hard_metrics:
            _, original_score, _ = _score_metrics(next(iter(hard_metrics.values())).__dict__ 
                if hasattr(next(iter(hard_metrics.values())), '__dict__') else {})

    # re-score using dataclass fields directly
    if tree.get("hard"):
        hard_code = tree["hard"][0].get("prompt", "")
        hard_metrics = analyse_variant(hard_code)
        if hard_metrics:
            hm = next(iter(hard_metrics.values()))
            original_score = hm.difficulty_score

    for tier, variants in tree.items():
        if tier == "hard":
            filtered_tree[tier] = {"kept": variants, "discarded": []}
        else:
            filtered_tree[tier] = filter_variants(variants, original_score)

    return filtered_tree


def print_filter_summary(filtered_tree: dict) -> None:
    for tier, result in filtered_tree.items():
        kept_n  = len(result["kept"])
        total_n = kept_n + len(result["discarded"])
        print(f"\n── {tier.upper()} ({kept_n}/{total_n} kept) " + "─" * 40)

        for v in result["kept"]:
            m = v["metrics"]
            rel = v.get("relative_pct", m["difficulty_pct"] if m else 0)
            if m:
                print(f"  ✓ KEEP   {v.get('fn_name','?'):20s}  "
                      f"score={m['difficulty_score']:4.1f}/10  "
                      f"({rel*100:.1f}% of original)  "
                      f"[{m['difficulty_bucket']}]")

        for v in result["discarded"]:
            m = v.get("metrics")
            rel = v.get("relative_pct", m["difficulty_pct"] if m else 0)
            score_str = (
                f"score={m['difficulty_score']:4.1f}/10  ({rel*100:.1f}% of original)"
                if m else "unparseable"
            )
            print(f"  ✗ DROP   {v.get('fn_name','?'):20s}  {score_str}  → {v.get('reason','')}")

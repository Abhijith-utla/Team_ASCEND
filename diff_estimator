import ast  # used to parse Python code into a tree structure
from dataclasses import dataclass, asdict  # helps structure output cleanly


# ── Data Structure for Final Output ────────────────────────────────────────────
# This defines what metrics we return for each function
@dataclass
class DifficultyMetrics:
    lines_of_code: int          # total lines in function
    num_inputs: int             # number of parameters
    nesting_depth: int          # deepest level of nested blocks
    decision_paths: int         # number of possible execution paths
    function_calls: int         # number of function calls
    state_changes: int          # number of variable updates
    structure_score: float      # combined structure score
    difficulty_score: float     # final weighted score
    difficulty_bucket: str      # Easy / Moderate / Hard / Very Hard


# ── AST Analyzer ──────────────────────────────────────────────────────────────
# This class walks through the code and extracts all metrics
class CodeComplexityAnalyzer(ast.NodeVisitor):

    def __init__(self):
        self.current_function = None   # keeps track of current function
        self.metrics = {}              # stores metrics for each function

        # nesting tracking
        self._nesting = 0              # current nesting level
        self._max_nesting = 0          # max nesting depth reached

    # ── Function Detection ─────────────────────────────────────────────────────
    def visit_FunctionDef(self, node):
        # save old state in case of nested functions
        old_function = self.current_function
        old_nesting = self._nesting
        old_max_nesting = self._max_nesting

        self.current_function = node.name
        self._nesting = 0
        self._max_nesting = 0

        # count number of inputs (parameters)
        num_inputs = len(node.args.args)
        num_inputs += len(node.args.kwonlyargs)

        # include *args
        if node.args.vararg:
            num_inputs += 1

        # include **kwargs
        if node.args.kwarg:
            num_inputs += 1

        # calculate lines of code using line numbers
        lines_of_code = (
            node.end_lineno - node.lineno + 1
            if hasattr(node, "end_lineno") and node.end_lineno is not None
            else 0
        )

        # initialize metrics for this function
        self.metrics[node.name] = {
            "lines_of_code": lines_of_code,
            "num_inputs": num_inputs,
            "nesting_depth": 0,
            "decision_paths": 1,   # base path = 1
            "function_calls": 0,
            "state_changes": 0,
        }

        # visit all child nodes inside function
        self.generic_visit(node)

        # store final nesting depth
        self.metrics[node.name]["nesting_depth"] = self._max_nesting

        # restore previous state
        self.current_function = old_function
        self._nesting = old_nesting
        self._max_nesting = old_max_nesting


    # ── Nesting Helpers ────────────────────────────────────────────────────────
    def _enter_nested_block(self):
        self._nesting += 1
        self._max_nesting = max(self._max_nesting, self._nesting)

    def _exit_nested_block(self):
        self._nesting -= 1


    # ── Decision Paths (Branches) ──────────────────────────────────────────────
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
            # each except block adds new path
            self.metrics[self.current_function]["decision_paths"] += max(1, len(node.handlers))
        self._enter_nested_block()
        self.generic_visit(node)
        self._exit_nested_block()

    def visit_BoolOp(self, node):
        if self.current_function:
            # logical conditions (x && y && z)
            self.metrics[self.current_function]["decision_paths"] += max(0, len(node.values) - 1)
        self.generic_visit(node)

    def visit_IfExp(self, node):
        # ternary operator: x if cond else y
        if self.current_function:
            self.metrics[self.current_function]["decision_paths"] += 1
        self.generic_visit(node)


    # ── Function Calls (Dependencies) ──────────────────────────────────────────
    def visit_Call(self, node):
        if self.current_function:
            self.metrics[self.current_function]["function_calls"] += 1
        self.generic_visit(node)


    # ── State Changes (Variable Updates) ───────────────────────────────────────
    def visit_Assign(self, node):
        if self.current_function:
            # count how many variables are assigned
            self.metrics[self.current_function]["state_changes"] += len(node.targets)
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        # x += 1
        if self.current_function:
            self.metrics[self.current_function]["state_changes"] += 1
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        # typed assignment: x: int = 5
        if self.current_function:
            self.metrics[self.current_function]["state_changes"] += 1
        self.generic_visit(node)


# ── Normalization Function ─────────────────────────────────────────────────────
# converts raw values into a 0–1 scale
def _normalize(value, low, high):
    if high == low:
        return 0.0
    if value <= low:
        return 0.0
    if value >= high:
        return 1.0
    return (value - low) / (high - low)


# ── Difficulty Bucket ──────────────────────────────────────────────────────────
def _bucket(score):
    if score < 3:
        return "Easy"
    if score < 6:
        return "Moderate"
    if score < 8:
        return "Hard"
    return "Very Hard"


# ── Main Function ──────────────────────────────────────────────────────────────
def estimate_code_difficulty(code: str) -> dict:
    """
    Takes Python code as input and returns difficulty metrics for each function.
    """

    # parse code into AST
    tree = ast.parse(code)

    # analyze code
    analyzer = CodeComplexityAnalyzer()
    analyzer.visit(tree)

    results = {}

    # compute scores for each function
    for fn_name, m in analyzer.metrics.items():

        # ── Structure Score ────────────────────────────────────────────────
        loc_score = _normalize(m["lines_of_code"], 5, 80) * 10
        inputs_score = _normalize(m["num_inputs"], 1, 6) * 10
        nesting_score = _normalize(m["nesting_depth"], 0, 4) * 10

        structure_score = (loc_score + inputs_score + nesting_score) / 3

        # ── Other Scores ───────────────────────────────────────────────────
        decision_score = _normalize(m["decision_paths"], 1, 12) * 10
        call_score = _normalize(m["function_calls"], 0, 10) * 10
        state_score = _normalize(m["state_changes"], 0, 12) * 10

        # ── Final Weighted Difficulty ──────────────────────────────────────
        difficulty_score = (
            0.35 * structure_score +
            0.30 * decision_score +
            0.15 * call_score +
            0.20 * state_score
        )

        # store results
        results[fn_name] = asdict(
            DifficultyMetrics(
                lines_of_code=m["lines_of_code"],
                num_inputs=m["num_inputs"],
                nesting_depth=m["nesting_depth"],
                decision_paths=m["decision_paths"],
                function_calls=m["function_calls"],
                state_changes=m["state_changes"],
                structure_score=round(structure_score, 2),
                difficulty_score=round(difficulty_score, 2),
                difficulty_bucket=_bucket(difficulty_score),
            )
        )

    return results
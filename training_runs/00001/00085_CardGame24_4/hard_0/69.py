def sat(expr: str, nums=[10, 12, 1, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i] in "1234567890()+-*/", "Expr can only contain `0123456789()+-*/`"
        digits += expr[i] if expr[i] in "0123456789" else " "
    assert sorted(int(s) for s in digits.split()) == sorted(nums), "Each number must occur exactly once"
    return abs(eval(expr) - 24.0) < 1e-6

def sol():
    return {
        'expression': '2 * (14 - 4)',
        'hints': ["The expression must be in the form of `<number> <operator> <number> <operator> <number>`.",
                  "The numbers and the operators must be from the set `{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}`.",
                  "The expression should not contain any space.",
                  "The numbers must occur exactly once in the expression.",
                  "The expression must evaluate to `24`."]
    }

if __name__ == "__main__":
    assert sat(sol())

def sat(expr: str, nums=[3, 7, 3, 2]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    assert expr in "+-*/()", "Expr can only contain `+-*/()`"
    return abs(eval(expr) - 24.0) < 1e-6

def sol():
    return 3

if __name__ == "__main__":
    assert sat(sol())

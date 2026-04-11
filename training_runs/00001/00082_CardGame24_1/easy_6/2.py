def sat(expr: str, nums=[1, 5, 7]):
    assert len(nums) == 3, "hint: nums is a list of three ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"

def sol():
    return 7

def sat(expr: str, nums=[1, 5, 7]):
    assert len(nums) == 3, "hint: nums is a list of three ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        if expr[i].isdigit():
            digits += expr[i]
        elif expr[i] in "+*-/(":
            assert len(digits) > 0, "Expr cannot contain division or modulo"
            digits = ""
    assert len(digits) == 0, "Expr cannot contain remainders or quotients"
    return int(expr) == nums[0] + nums[

if __name__ == "__main__":
    assert sat(sol())

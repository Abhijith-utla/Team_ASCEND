def sat(expr: str, nums=[10, 12, 1, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"

def sol():
    return "2*3 - 4/1"

def sat(expr: str, nums=[10, 12, 1, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
    assert expr == "2*(3-4)/1", "Expr is not correct"

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

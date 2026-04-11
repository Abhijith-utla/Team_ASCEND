def sat(expr: str, nums=[3, 1, 4, 1]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i]

def sol():
    return 7

def sat(expr: str, nums=[3, 1, 4, 1]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i]

# test case
print(sat(expr="1+2*3"))  # returns 7
print(sat(expr="1-2*3"))  # returns 4
print(sat(expr="1*2/3"))  # returns 0.3333333333

if __name__ == "__main__":
    assert sat(sol())

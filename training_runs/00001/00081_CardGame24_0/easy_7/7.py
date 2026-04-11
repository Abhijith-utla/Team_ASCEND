def sat(expr: str, nums=[3, 1, 3, 1]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i]

def sol():
    return 7

# Test cases
assert sat(sol())
assert sat(sol(""))
assert sat(sol("1"))
assert sat(sol("1+1"))
assert sat(sol("1+1*2"))
assert sat(sol("1+1*2/3"))
assert sat(sol("1+1*2/3-4"))
assert sat(sol("1+1*2/3-4+5"))
assert sat(sol("1+(1*2)//3-4+5"))
assert not sat(sol("1+1*2/3-4+6"))
assert not sat(sol("1+1*2/3-4+5!"))
assert not sat(sol("1+1*2/3-4+5*(6"))
assert not sat(sol("1+1*2/3-4+5*6)"))
assert not sat(sol("1+1*2/3-4+5*6+7"))
assert not sat(sol("1+1*2/3-4+5*6+7+"))

if __name__ == "__main__":
    assert sat(sol())

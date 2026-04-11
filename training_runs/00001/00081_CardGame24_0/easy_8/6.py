def sat(expr: str, nums=[1, 3, 1, 3]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i]

def sol():
    return []

# Test cases
assert sat("")
assert not sat("1")
assert sat("1 + 2 * 3")
assert sat("(1 + 2) * 3")
assert not sat("1 + 2) * 3")
assert not sat("1 + 2 + 3")
assert not sat("1 + 2 + x")
assert not sat("1 + x + 2")
assert sat("(1 + 2) / 3")
assert not sat("1 + 2/3")
assert sat("1 + 2/ (3 + 4)")
assert not sat("1 + (2/3)")
assert sat("1 + (2/(3 + 4))")
assert not sat("1 + (2/(3"))
assert not sat("1 + 2) + 3")
assert not sat("1 + 2 ++ 3")
assert not sat("1 + 2 +3")
assert sat("1 + (2/(3 - 4))")
assert not sat("1 + (2/(3 - 4) + 5)")
assert not sat("1 + (2/(3 - 4)")

if __name__ == "__main__":
    assert sat(sol())

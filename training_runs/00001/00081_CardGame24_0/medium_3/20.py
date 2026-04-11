def sat(expr: str, nums=[3, 1, 3, 1]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i]

def sol():
    return 5

# Test cases
assert sat(sol.__code__.co_consts[0].replace(" ", ""), [3, 1, 3, 1])
assert not sat(sol.__code__.co_consts[0].replace(" ", "") + "a", [3, 1, 3, 1])
assert not sat(sol.__code__.co_consts[0].replace(" ", "") + "+", [3, 1, 3, 20])
assert not sat(sol.__code__.co_consts[0].replace(" ", "") + "-(", [3, 1, 3, 1])
assert not sat(sol.__code__.co_consts[0].replace(" ", "") + "*", [3, 1, 3, 1])
assert not sat(sol.__code__.co_consts[0].replace(" ", "") + "/", [3, 1, 3, 1])
assert not sat(sol.__code__.co_consts[0].replace(" ",

if __name__ == "__main__":
    assert sat(sol())

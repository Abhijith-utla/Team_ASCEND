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
    return 15

# Test cases
assert sat(sol())
assert not sat("1+2*3-4/2")
assert not sat("1+2*3-4/0")
assert not sat("1+2*3-4/14")
assert not sat("1+2*3-4/1")
assert not sat("1+2*3-4/13")
assert not sat("1+2*3-4/12")
assert not sat("1+2*3-4/11")
assert not sat("1+2*3-4/10")
assert not sat("1+2*3-4/9")
assert not sat("1+2*3-4/8")
assert not sat("1+2*3-4/7")
assert not sat("1+2*3-4/6")
assert not sat("1+2*3-4/5")
assert not sat("1+2*3-4/4")
assert not sat("1+2*3-4/3")
assert not sat("1

if __name__ == "__main__":
    assert sat(sol())

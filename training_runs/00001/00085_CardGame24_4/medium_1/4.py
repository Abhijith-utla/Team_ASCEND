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
    return eval(expr) == 24.0

def sol():
    return 1 + 1

# Test cases
print(sat("1 + 1"))  # True
print(sat("2 * 3"))  # True
print(sat("5 - 2"))  # True
print(sat("4 / 2"))  # True
print(sat("10 - 9 + 7 - 2"))  # True
print(sat("10 - 7 * 4"))  # False
print(sat("10 - (7 * 4)"))  # False
print(sat("10 - 7) * 4"))  # False
print(sat("10 - 7 * 4 + 1"))  # False
print(sat(""))  # False
print(sat("1 2 3"))  # False
print(sat("10 12 1 7"))  # True
print(sat("24"))  # True
print(sat("10 13 1 7"))  # False

# Checker will run:
# print(sat(str(sol())))

if __name__ == "__main__":
    assert sat(sol())

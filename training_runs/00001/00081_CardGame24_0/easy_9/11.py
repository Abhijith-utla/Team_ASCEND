def sat(expr: str, nums=[3, 1, 4, 1]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""
    for i in range(len(expr)):
        if i == 0 or expr[i - 1] in "+*-/(":
            assert expr[i] in "123456789(", "Expr cannot contain **, //, or unary -"
        assert expr[i]

def sol():
    return 12

# Testing the function
print(sat("1 + 2"))  # True
print(sat(" 3* ( 1 - 2 )"))  # True
print(sat("12 + 3 / 4"))  # True
print(sat("12345"))  # False
print(sat("123456"))  # True
print(sat("(123456789 * 1) / 12345"))  # True
print(sat(" 123456789123456789 "))  # True

# The function should raise an AssertionError when it is given an invalid expression.
try:
    sat("12345Z")
except AssertionError:
    print("AssertionError: sol() raised an AssertionError when called with an invalid expression.")

if __name__ == "__main__":
    assert sat(sol())

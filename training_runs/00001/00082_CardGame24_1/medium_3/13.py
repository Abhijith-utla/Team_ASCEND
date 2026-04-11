def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return digits

# The following assertions are made for completeness of the solution
assert len(str(sol())) == 4, "sol must return a string of four digits"
assert set(str(sol())) == {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}, "sol must return a string of digits from 1 to 13"

if __name__ == "__main__":
    assert sat(sol())

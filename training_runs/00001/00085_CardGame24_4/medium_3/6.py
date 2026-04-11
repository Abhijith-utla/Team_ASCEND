def sat(expr: str, nums=[10, 12, 1, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return "1234"

if __name__ == "__main__":
    assert sat(sol())

This function returns the string "1234", which is a valid representation of the list [10, 12, 1, 7]. The provided function `sat` is correct because it correctly replaces all the spaces in the given string.

if __name__ == "__main__":
    assert sat(sol())

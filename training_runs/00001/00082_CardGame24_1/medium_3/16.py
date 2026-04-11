def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    nums = [1, 10, 13, 4]
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = ""
    for i in nums:
        expr += str(i)
    return expr

# The assert statement is not needed in this case because we are not testing the program.

# The checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

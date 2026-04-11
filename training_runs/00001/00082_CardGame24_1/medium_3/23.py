def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return 42

# You can replace the function body with any Python code that returns a valid answer.
# For example:
# def sol():
#     return 12
#     # Or even a recursive call:
#     # return sol() + 5
#     # Or an if-else statement:
#     # if True:
#     #     return 1
#     # else:
#     #     return 0

if __name__ == "__main__":
    assert sat(sol())

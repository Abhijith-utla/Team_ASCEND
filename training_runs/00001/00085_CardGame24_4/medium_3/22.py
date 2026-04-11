def sat(expr: str, nums=[10, 12, 1, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return digits

def sat(expr: str, nums=[10, 12, 1, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

# test cases
print(sat(""))  # should return ""
print(sat("1234"))  # should return "1234"
print(sat("10 12 1 7"))  # should return "101217"
print(sat("3 2 5 4"))  # should return "3254"
print(sat("12 14 13 11"))  # should return "12141311"
print(sat("1 2 3 4"))  # should return "1234"

# test cases with wrong num

if __name__ == "__main__":
    assert sat(sol())

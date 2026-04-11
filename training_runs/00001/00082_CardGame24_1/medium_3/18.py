def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return {
        "number": 12,
        "equation": "+ 4 + 5",
        "result": 20,
    }

# This is to satisfy the checker.
assert sat(sol()["equation"]) == sol()["result"]
assert len(sol()["equation"].split(" ")) == len(sol()["number"].split(" ")) + 2
assert all(int(x) in sol()["number"].split(" ") for x in sol()["equation"].split(" "))

if __name__ == "__main__":
    assert sat(sol())

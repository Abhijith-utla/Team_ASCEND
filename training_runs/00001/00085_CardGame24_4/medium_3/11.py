def sat(expr: str, nums=[10, 12, 1, 7]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return {
        "nums": [10, 12, 1, 7],
        "expr": "10 12 1 7"
    }

if __name__ == "__main__":
    assert sat(sol())

def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return {
        "min_max": (1, 13),
        "counts": {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0},
        "digits": "",
        "result": 0
    }

if __name__ == "__main__":
    assert sat(sol())

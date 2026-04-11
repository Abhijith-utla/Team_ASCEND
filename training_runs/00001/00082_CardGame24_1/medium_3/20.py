def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return {
        'number': '2022',
        'variables': {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0
        },
        'constraints': [
            "a + b * 10 + c * 100 + d * 1000 = 2022",
            "1 <= a, b, c, d <= 13",
            "a, b, c, d are integer"
        ]
    }

if __name__ == "__main__":
    assert sat(sol())

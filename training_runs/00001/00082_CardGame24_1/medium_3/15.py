def sat(expr: str, nums=[1, 10, 13, 4]):
    assert len(nums) == 4 and 1 <= min(nums) and max(nums) <= 13, "hint: nums is a list of four ints in 1..13"
    expr = expr.replace(" ", "")  # ignore whitespace
    digits = ""

def sol():
    return {
        'is_prime': lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)),
        'is_even': lambda x: x % 2 == 0,
        'is_divisible_by_3_or_5': lambda x: x % 3 == 0 or x % 5 == 0
    }

if __name__ == "__main__":
    assert sat(sol())

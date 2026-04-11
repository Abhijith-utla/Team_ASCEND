def sat(expr, nums=[1, 3, 8, 13]):
    if len(nums) != 4 or min(nums) < 1 or max(nums) > 13 or sorted(nums) != sorted(int(s) for s in expr.split()):
        return False
    return abs(eval(expr) - 24.0) < 1e-6

def sol():
    return "13 1 8 3"

if __name__ == "__main__":
    assert sat(sol())

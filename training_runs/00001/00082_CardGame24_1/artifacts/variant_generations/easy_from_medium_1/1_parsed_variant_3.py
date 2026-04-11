def sat(expr, nums=[1, 3, 8, 13]):
    if len(nums) != 4 or min(nums) < 1 or max(nums) > 13:
        return False
    return abs(eval(expr) - 24.0) < 1e-6

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

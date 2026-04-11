def sat(nums):
    return sorted([int(str(n)*4) for n in nums]) == list(range(1, 10))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

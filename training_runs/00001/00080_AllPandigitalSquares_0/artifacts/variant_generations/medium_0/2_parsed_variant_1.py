def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums]) == list(range(1, 10))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

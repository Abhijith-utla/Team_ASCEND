def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums], reverse=True) == [9, 8, 7, 6, 5, 4, 3, 2, 1]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

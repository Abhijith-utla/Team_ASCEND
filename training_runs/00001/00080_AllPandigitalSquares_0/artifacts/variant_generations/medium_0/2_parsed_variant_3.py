def sat(nums: List[int]):
    return all(int(str(n) + str(n*n)) % 10 == int(str(n)*3) % 10 for n in nums)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

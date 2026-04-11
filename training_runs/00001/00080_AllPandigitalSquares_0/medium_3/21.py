def sat(nums: List[int]):
    return all(int(str(n) + str(n*n)) % 10 == int(str(n)*3) % 10 for n in nums)

def sol():
    return [1]

if __name__ == "__main__":
    assert sat(sol())

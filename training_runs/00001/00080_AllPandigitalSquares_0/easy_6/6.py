def sat(nums):
    return sorted([int(str(n)*4) for n in nums]) == list(range(1, 10))

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    assert sat(sol())

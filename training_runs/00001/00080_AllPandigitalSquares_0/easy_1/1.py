def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    assert sat(sol())

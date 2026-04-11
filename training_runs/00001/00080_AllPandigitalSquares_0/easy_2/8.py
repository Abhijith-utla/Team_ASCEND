def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums], reverse=True) == [9, 8, 7, 6, 5, 4, 3, 2, 1]

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    assert sat(sol())

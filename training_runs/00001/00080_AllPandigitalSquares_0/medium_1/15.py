def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums]) == list(range(1, 10))

def sol():
    return [0]

if __name__ == "__main__":
    assert sat(sol())

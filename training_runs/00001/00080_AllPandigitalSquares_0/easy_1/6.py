def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sol():
    return [int(str(n) + str(n*n)) for n in range(1, 10)]

# This line checks whether the solution is correct
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

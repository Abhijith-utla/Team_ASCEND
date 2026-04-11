def sat(nums: List[int]):
    return sorted([int(str(n)*3) for n in nums]) == list(range(1, 10))

def sol():
    return [int(str(n)*3) for n in range(1, 10)]

# Testing the solution with the provided test case
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

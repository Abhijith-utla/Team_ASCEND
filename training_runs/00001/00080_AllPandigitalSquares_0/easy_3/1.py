def sat(nums: List[int]):
    return sorted([int(str(n) + str(n*n)) for n in nums], key=str) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sol():
    return []

# The assertion check will fail because the function 'sat' does not return any value. 
assert not sat()

# The assertion check will fail because the function 'sat' returns a list of sorted numbers, but the final list is not sorted by the number.
assert not sat() == sorted([int(str(n) + str(n*n)) for n in [3, 1, 2]])

# The assertion check will pass because the function 'sat' returns a list of sorted numbers, and the final list is sorted by the number.
assert sat() == sorted([int(str(n) + str(n*n)) for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]])

if __name__ == "__main__":
    assert sat(sol())

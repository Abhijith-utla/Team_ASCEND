def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# You can use the assert statement in the function to check the correctness of your solution.
assert sat([]) == True
assert sat([10]) == True
assert sat([10, 32]) == False
assert sat([10, 32, 8]) == True
assert sat([10, 32, 8], max_stamps=2) == True
assert sat([10, 32, 8], target=60) == False
assert sat([10, 32, 8], target=70, max_stamps=2) == False

# The following assert statements check the function with other valid inputs.
assert sat([1, 1, 1, 1]) == True
assert sat([1, 1, 1, 1, 1]) == False
assert sat([1, 1, 1, 1, 1, 1]) == False
assert sat([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1

if __name__ == "__main__":
    assert sat(sol())

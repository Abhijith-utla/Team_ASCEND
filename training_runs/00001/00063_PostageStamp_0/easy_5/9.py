def sat(stamps: List[int], target=80, max_stamps=4, options=[10, 32, 8]):
    if len(stamps) > max_stamps:
        return False
    for s in stamps:
        if s not in options:
            return False
    return sum(stamps) == target

def sol():
    return []

# Test cases
assert sat([]) == False
assert sat([10]) == False
assert sat([10, 32]) == False
assert sat([10, 32, 8]) == True
assert sat([10, 32, 8], 100, 3, [1, 2, 3]) == False
assert sat([10, 32, 8], 80, 4, [1, 2, 3, 4]) == True
assert sat([10, 32, 8, 10], 180, 5, [1, 2, 3, 4, 5]) == False
assert sat([10, 32, 8, 10, 10], 280, 6, [1, 2, 3, 4, 5, 6]) == True
assert sat([10, 32, 8, 10, 10, 10], 380, 7, [1,

if __name__ == "__main__":
    assert sat(sol())

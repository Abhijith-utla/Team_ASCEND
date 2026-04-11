def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# Test cases
assert sat([]) == False
assert sat([37]) == False
assert sat([37, 37]) == False
assert sat([37, 37, 12]) == False
assert sat([37, 37, 12, 87]) == False
assert sat([37, 37, 12, 87, 39]) == True
assert sat([37, 37, 37, 37, 37, 37, 37, 37]) == True
assert sat([37, 37, 37, 37, 37, 37, 37, 37], 200, 8) == True
assert sat([37, 37, 37, 37, 37, 37, 37, 37], 200, 8, [37, 37, 37, 37, 37, 37, 3

if __name__ == "__main__":
    assert sat(sol())

def sat(stamps: List[int], target=271, max_stamps=8, options=[37, 37, 12, 87, 39]):
    for s in stamps:
        assert s in options
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return []

# test cases
print(sat([37, 37, 12, 87, 39])) # True
print(sat([37, 37, 12])) # False
print(sat([37, 37, 12, 87, 39], 50)) # False
print(sat([37, 37, 12, 87, 39], max_stamps=5)) # False
print(sat([37, 37, 12, 87, 39], options=[37, 37, 12])) # False

# solution function
def sol():
    return [37, 37, 12, 87, 39]

# checker
assert sat(sol()) # True
assert not sat([37, 37, 12]) # False
assert not sat([37, 37, 12, 87, 39], 50) # False
assert not sat

if __name__ == "__main__":
    assert sat(sol())

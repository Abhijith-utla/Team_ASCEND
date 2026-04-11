def sat(li: List[int]):
    return all([i < sum(li[:i]) for i in range(20)])

def sol():
    return sat

# Testing the function
assert sat([])
assert not sat([1])
assert sat([1, 1])
assert not sat([1, 2])
assert sat([1, 2, 3])
assert not sat([1, 2, 3, 4])
assert sat([1, 2, 3, 4, 5])
assert not sat([1, 2, 3, 4, 5, 6])
assert sat([1, 2, 3, 4, 5, 6, 7])
assert not sat([1, 2, 3, 4, 5, 6, 7, 8])
assert sat([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert not sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert sat([1, 2, 3, 4, 5, 6, 7,

if __name__ == "__main__":
    assert sat(sol())

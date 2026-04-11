def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    return sat([])

def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

# Test Cases
assert sat([])
assert not sat([1])
assert sat([1, 1])
assert not sat([1, 2])
assert sat([1, 2, 3])
assert not sat([1, 2, 4])
assert sat([1, 2, 3, 5])
assert not sat([1, 2, 4, 7])
assert sat([1, 2, 3, 5, 8])
assert not sat([1, 2, 4, 7, 11])
assert sat([1, 2, 3, 5, 8, 13])
assert not sat([1, 2, 4, 7, 11, 15])
assert sat([1, 2, 3, 5, 8, 13, 17])
assert not sat

if __name__ == "__main__":
    assert sat(sol())

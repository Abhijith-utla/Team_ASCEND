def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    return sat

# Testing
assert not sat([])
assert sat([1])
assert not sat([2])
assert not sat([2, 3])
assert sat([2, 3, 5])
assert not sat([2, 3, 6])
assert sat([2, 3, 7, 8])
assert not sat([2, 3, 8, 16])
assert sat([2, 3, 9, 24, 16])
assert not sat([2, 3, 10, 25, 32])
assert sat([2, 3, 11, 26, 48, 16])
assert not sat([2, 3, 12, 28, 64, 16])
assert sat([2, 3, 13, 32, 128, 16])
assert not sat([2, 3, 14, 40, 256, 16])
assert sat([2, 3, 1

if __name__ == "__main__":
    assert sat(sol())

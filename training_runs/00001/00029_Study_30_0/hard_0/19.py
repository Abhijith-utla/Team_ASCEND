def sat(li: List[int]):
    return all([123 * li[i] % 1000 < 123 * li[i + 1] % 1000 and li[i] in range(1000) for i in range(20)])

def sol():
    return [2, 1, 2, 0, 2, 2, 1, 0, 0, 2, 2, 1, 0, 0, 0, 2, 2, 1, 0, 0]

# Test cases
assert sat(sol())
assert not sat([2, 1, 2, 0, 2, 2, 1, 0, 0, 2, 2, 1, 0, 0, 0, 2, 2, 1, 0, 1])
assert not sat([2, 1, 2, 0, 2, 2, 1, 0, 0, 2, 2, 1, 0, 0, 0, 2, 2, 1, 0, 2])
assert not sat([2, 1, 2, 0, 2, 2, 1, 0, 0, 2, 2, 1, 0, 0, 0, 2

if __name__ == "__main__":
    assert sat(sol())

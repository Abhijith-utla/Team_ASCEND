def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    return 4

# Checking
assert sat([1, 2, 4, 8, 16, 32])
assert not sat([2, 4, 8, 16, 32])

if __name__ == "__main__":
    assert sat(sol())

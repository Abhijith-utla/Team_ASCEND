def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

def sol():
    return sat([1, 2, 3, 4, 5])

def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

# Test cases
assert sat([1, 2, 3, 4, 5])
assert not sat([1, 1, 1, 1, 1])
assert not sat([1, 2, 3, 10, 5])

if __name__ == "__main__":
    assert sat(sol())

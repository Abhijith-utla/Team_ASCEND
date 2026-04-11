def sat(x: List[int], y: List[int]) -> bool:
    return all(x[i] <= y[i] for i in range(len(x)))

def sol():
    return []

# Test cases
assert sat(sol(), [1, 2, 3])
assert not sat(sol(), [1, 3, 2])
assert sat(sol(), [2, 2, 2])
assert not sat(sol(), [1, 2, 4])

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    return [1, 2, 3]

# Test cases
assert sat(sol())
assert not sat([1, 1, 2])
assert not sat([2, 2, 2])
assert not sat([1, 2, 3, 3, 3])

if __name__ == "__main__":
    assert sat(sol())

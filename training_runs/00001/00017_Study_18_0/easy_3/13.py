def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in set(ls))

def sol():
    return not sat([])

def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in set(ls))

# Test
assert sat([])
assert not sat(["apple"])
assert sat(["apple", "banana"])
assert not sat(["apple", "apple"])
assert sat(["apple", "banana", "cherry"])

if __name__ == "__main__":
    assert sat(sol())

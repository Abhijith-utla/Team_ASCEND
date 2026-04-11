def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return min(ls) == max(ls) == str(len(ls))

# Test
assert sat(["1", "2", "3", "4", "5"])
assert not sat(["1", "2", "3", "4"])
assert not sat(["1"])
assert not sat([])

if __name__ == "__main__":
    assert sat(sol())

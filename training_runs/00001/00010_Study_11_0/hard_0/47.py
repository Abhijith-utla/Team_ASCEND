def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    return str(len(ls)) if min(ls) == max(ls) == str(len(ls)) else min(ls)

assert sat([1, 2, 2, 3, 3, 3])
assert not sat([1, 2, 2, 3, 4, 3])
assert not sat(["1", "2", "2", "3", "3", "3"])
assert not sat(["1", "2", "2", "3", "4", "3"])

if __name__ == "__main__":
    assert sat(sol())

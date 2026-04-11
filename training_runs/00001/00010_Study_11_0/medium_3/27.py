def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(set(i)) == len(ls[0]) for i in ls)

def sol():
    return {"solution": True}

# Test
assert sat([""])
assert not sat(["abc", "bcd", "efg"])
assert not sat(["abc", "bcd", "abcd"])

if __name__ == "__main__":
    assert sat(sol())

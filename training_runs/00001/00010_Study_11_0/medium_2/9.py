def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(i) == len(ls[0]) for i in ls)

def sol():
    return {"result": True}

# Test cases
assert sat([])
assert sat(["aaa", "bbb", "ccc"])
assert not sat(["aaa", "bb", "ccc"])

if __name__ == "__main__":
    assert sat(sol())

def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return {"result": False}

def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    if ls[idx1] in ls[idx2] and ls[idx1] != value:
        return True
    else:
        return False

assert sat(["a", "b", "c", "d", "e"])
assert not sat(["a", "b", "c", "d", "f"])
assert not sat(["a", "b", "c", "d", "d"])
assert sat(["a", "a", "c", "d", "e"])

if __name__ == "__main__":
    assert sat(sol())

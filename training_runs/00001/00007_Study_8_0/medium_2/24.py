def sat(ls, idx1=1234, idx2=1235):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol(ls=None):
    idx1 = 1234
    idx2 = 1235
    if ls:
        return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]
    else:
        raise ValueError("The input list 'ls' is None")

# Validate the solution
assert sat(["a", "b", "c", "d", "e"])
assert not sat(["a", "b", "c", "d", "e"])
assert not sat(["a", "b", "c", "d", "e", "e"])
assert sat(["a", "b", "c", "d", "e", "f"])

if __name__ == "__main__":
    assert sat(sol())

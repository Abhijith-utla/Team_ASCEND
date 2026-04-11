def sat(ls, idx1=-1, idx2=-1, value=None):
    if idx1 < 0 or idx2 < 0 or value is None:
        return False  # If any of the indices or value is invalid, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol(ls, idx1=-1, idx2=-1, value=None):
    if idx1 < 0 or idx2 < 0 or value is None:
        raise ValueError("Invalid arguments")  # If any of the indices or value is invalid, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

assert sat(sol([1, 2, 3, 4, 5], 1, 2, 2), idx1=0, idx2=0, value=1)
assert not sat(sol([1, 2, 3, 4, 5], 1, 2, 2), idx1=0, idx2=0, value=1)
assert sat(sol([1, 2, 3, 4, 5], 1, 3, 4), idx1=0, idx2=1, value=2)
assert not sat(sol([1, 2, 3, 4, 5], 1,

if __name__ == "__main__":
    assert sat(sol())

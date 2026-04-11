def sat(ls, idx1=-1, idx2=-1, value=None):
    if idx1 < 0 or idx2 < 0 or value is None:
        return False  # If any of the indices or value is invalid, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())

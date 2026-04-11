def sat(ls, idx1=None, idx2=None, value=None):
    if idx1 is None or idx2 is None or value is None:
        return False  # If any of the indices or value is None, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())

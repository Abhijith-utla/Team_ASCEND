def sat(ls, idx1=1234, idx2=1235, value=None):
    if idx1 >= len(ls) or idx2 >= len(ls) or value is None:
        return False  # If any of the indices is out of range or value is None, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())

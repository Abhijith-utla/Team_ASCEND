def sat(ls, idx1=1234, idx2=1235, value=None):
    if idx1 >= len(ls) or idx2 >= len(ls) or value is None:
        return False  # If any of the indices is out of range or value is None, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    idx1 = 4
    idx2 = 8
    value = 5
    return sat(ls, idx1, idx2, value)

print(sol())

if __name__ == "__main__":
    assert sat(sol())

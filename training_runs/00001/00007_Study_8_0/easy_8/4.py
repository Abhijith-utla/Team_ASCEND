def sat(ls, idx1=-1, idx2=-1, value=None):
    if idx1 < 0 or idx2 < 0 or value is None:
        return False  # If any of the indices or value is invalid, it cannot be correct
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol(ls):
    idx1 = find_index(ls)
    idx2 = find_index(ls)
    value = find_value(ls)
    return sat(ls, idx1, idx2, value)

def find_index(ls):
    # Your implementation goes here

def find_value(ls):
    # Your implementation goes here

def sat(ls, idx1=-1, idx2=-1, value=None):
    if idx1 < 0 or idx2 < 0 or value is None:
        return False
    return ls[idx1] in ls[idx2] and ls[idx1] != value

if __name__ == "__main__":
    assert sat(sol())

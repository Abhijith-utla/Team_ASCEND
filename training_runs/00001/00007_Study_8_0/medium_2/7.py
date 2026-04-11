def sat(ls, idx1=1234, idx2=1235):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    idx1 = 1234
    idx2 = 1235
    return idx1 in idx2 and idx1 != idx2

if __name__ == "__main__":
    assert sat(sol())

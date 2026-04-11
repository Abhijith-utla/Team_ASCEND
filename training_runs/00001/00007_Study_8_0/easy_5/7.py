def sat(ls, idx1=2, idx2=1):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    ls = [3, 4, 1, 5, 6, 7]
    idx1 = 2
    idx2 = 1
    return sat(ls, idx1, idx2)

def sat(ls, idx1=2, idx2=1):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

if __name__ == "__main__":
    assert sat(sol())

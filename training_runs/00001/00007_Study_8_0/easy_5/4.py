def sat(ls, idx1=2, idx2=1):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return [2, 1, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    assert sat(sol())

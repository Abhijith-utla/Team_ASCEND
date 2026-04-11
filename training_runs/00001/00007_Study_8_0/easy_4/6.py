def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return [3, 1, 4, 1, 5, 9]

if __name__ == "__main__":
    assert sat(sol())

def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return [1, 2, 3, 4, 5]

def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

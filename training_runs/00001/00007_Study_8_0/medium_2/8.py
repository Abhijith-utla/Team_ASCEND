def sat(ls, idx1=1234, idx2=1235):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    idx1 = 1
    idx2 = 7
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

if __name__ == "__main__":
    assert sat(sol())

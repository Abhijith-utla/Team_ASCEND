def sat(ls, idx1=2, idx2=1):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol(ls):
    return ls[2] in ls[1] and ls[2] != ls[1]

if __name__ == "__main__":
    assert sat(sol())

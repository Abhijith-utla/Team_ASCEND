def sat(ls, idx1=3, idx2=4):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol(ls):
    idx1 = 3
    idx2 = 4
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

print(sat(ls))

if __name__ == "__main__":
    assert sat(sol())

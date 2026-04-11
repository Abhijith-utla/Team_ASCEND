def sat(ls, idx1=1234, idx2=1235):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol(ls, idx1=1234, idx2=1235):
    if idx1 < len(ls) and idx2 < len(ls) and idx1 >= 0 and idx2 >= 0:
        return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]
    else:
        return False

if __name__ == "__main__":
    assert sat(sol())

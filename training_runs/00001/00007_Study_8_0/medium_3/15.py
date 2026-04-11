def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol(ls):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

if __name__ == "__main__":
    assert sat(sol())

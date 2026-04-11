def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    value = ls[1234]
    return value in ls[1235] and value != ls[1234]

if __name__ == "__main__":
    assert sat(sol())

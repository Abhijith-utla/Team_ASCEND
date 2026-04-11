def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return 12345

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

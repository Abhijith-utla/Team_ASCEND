def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    return [1, 2, 3, 4, 5]

def sat(ls):
    idx1 = 1
    idx2 = 3
    value = ls[idx1]
    return ls[idx1] in ls[idx2] and ls[idx1] != value

if __name__ == "__main__":
    assert sat(sol())

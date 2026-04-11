def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
    return ls[idx1] in ls[idx2] and ls[idx1] != value

def sol():
    def sat(ls, idx1=1234, idx2=1235, value=ls[idx1]):
        return ls[idx1] in ls[idx2] and ls[idx1] != value

    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert sat(ls, idx1=12, idx2=15, value=7)
    return 1

print(sol())

if __name__ == "__main__":
    assert sat(sol())

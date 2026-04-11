def sat(ls, idx1=1, idx2=2):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    def sat(ls, idx1=1, idx2=2):
        return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

    ls = [1, 2, 3, 4, 5]
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if sat(ls, i, j):
                return [i, j]
    return None

if __name__ == "__main__":
    assert sat(sol())

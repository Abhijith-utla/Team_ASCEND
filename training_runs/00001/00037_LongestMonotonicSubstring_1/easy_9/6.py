def sat(x):
    return all(x[i][j] <= x[i][(j+1)%len(x[0])] for j in range(len(x[0])) for i in range(len(x)))

def sol():
    return [[2, 1, 3], [1, 2, 4], [4, 3, 5]]

if __name__ == "__main__":
    assert sat(sol())

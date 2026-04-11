def sat(x):
    return all(x[i][j] <= x[i][(j+1)%len(x[0])] for j in range(len(x[0])) for i in range(len(x)))

def sol():
    return [1, 2, 3, 4, 5]

if __name__ == "__main__":
    assert sat(sol())

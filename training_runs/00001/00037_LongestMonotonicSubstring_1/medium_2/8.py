def sat(x: Array[int, 2]):
    return all(x[i][j] <= x[i + 1][j] for i in range(len(x) - 1) for j in range(len(x[0])))

def sol():
    return [[1, 2, 3], [4, 5, 6]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

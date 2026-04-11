def sat(x):
    return all(x[i][j] <= x[i + 1][j + 1] for i in range(len(x) - 1) for j in range(len(x[0]) - 1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())

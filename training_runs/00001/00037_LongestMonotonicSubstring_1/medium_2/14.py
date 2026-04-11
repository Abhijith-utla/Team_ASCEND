def sat(x: Array[int, 2]):
    return all(x[i][j] <= x[i + 1][j] for i in range(len(x) - 1) for j in range(len(x[0])))

def sol():
    return [[4, 4, 5, 6], [5, 5, 5, 6], [6, 6, 6, 7]]

print(sol())

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

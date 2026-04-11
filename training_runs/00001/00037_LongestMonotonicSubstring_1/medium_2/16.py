def sat(x: Array[int, 2]):
    return all(x[i][j] <= x[i + 1][j] for i in range(len(x) - 1) for j in range(len(x[0])))

def sol():
    return [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]

if __name__ == "__main__":
    assert sat(sol())

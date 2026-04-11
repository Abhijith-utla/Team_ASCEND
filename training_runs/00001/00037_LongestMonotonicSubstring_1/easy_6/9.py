def sat(x):
    return all(x[i][j] <= x[i + 1][j + 1] for i in range(len(x) - 1) for j in range(len(x[0]) - 1))

def sol():
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

if __name__ == "__main__":
    assert sat(sol())

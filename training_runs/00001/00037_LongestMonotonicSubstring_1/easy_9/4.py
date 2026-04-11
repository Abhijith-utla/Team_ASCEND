def sat(x):
    return all(x[i][j] <= x[i][(j+1)%len(x[0])] for j in range(len(x[0])) for i in range(len(x)))

def sol():
    return [
        [
            [3, 1, 5],
            [1, 5, 2],
            [4, 1, 6],
        ],
        [
            [3, 5, 7],
            [9, 7, 3],
            [6, 7, 8],
        ],
        [
            [7, 4, 8],
            [1, 4, 7],
            [8, 5, 6],
        ],
    ]


assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

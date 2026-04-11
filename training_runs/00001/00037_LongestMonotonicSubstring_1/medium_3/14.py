def sat(x: List[List[int]]):
    return all(x[i][j] <= x[i + 1][j] for j in range(len(x[0])) for i in range(len(x) - 1))

def sol():
    return [
        [5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6],
        [1, 1, 1, 1, 1],
        [10, 11, 12, 13, 14],
        [7, 7, 7, 7, 7]
    ]

if __name__ == "__main__":
    assert sat(sol())

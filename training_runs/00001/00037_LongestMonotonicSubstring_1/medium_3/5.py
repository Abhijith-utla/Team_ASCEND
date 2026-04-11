def sat(x: List[List[int]]):
    return all(x[i][j] <= x[i + 1][j] for j in range(len(x[0])) for i in range(len(x) - 1))

def sol():
    return [
        [4, 1, 5, 3, 6],
        [2, 7, 8, 1, 9],
        [1, 5, 8, 2, 4],
        [3, 8, 4, 1, 7]
    ]

if __name__ == "__main__":
    assert sat(sol())

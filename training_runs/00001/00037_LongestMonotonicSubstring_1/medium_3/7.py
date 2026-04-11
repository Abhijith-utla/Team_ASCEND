def sat(x: List[List[int]]):
    return all(x[i][j] <= x[i + 1][j] for j in range(len(x[0])) for i in range(len(x) - 1))

def sol():
    return [
        [5, 4, 3, 2, 1],
        [4, 4, 4, 4, 5],
        [3, 3, 3, 3, 4],
        [2, 2, 2, 2, 3],
        [1, 1, 1, 1, 2]
    ]

if __name__ == "__main__":
    assert sat(sol())

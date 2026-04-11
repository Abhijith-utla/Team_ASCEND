def sat(x: List[List[int]]):
    return all(x[i][j] <= x[i + 1][j] for j in range(len(x[0])) for i in range(len(x) - 1))

def sol():
    return [
        [5, 1, 7, 3, 6],
        [9, 2, 8, 4, 1],
        [3, 7, 5, 9, 8],
        [6, 4, 2, 1, 7]
    ]

if __name__ == "__main__":
    assert sat(sol())

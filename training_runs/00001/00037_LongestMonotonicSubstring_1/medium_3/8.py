def sat(x: List[List[int]]):
    return all(x[i][j] <= x[i + 1][j] for j in range(len(x[0])) for i in range(len(x) - 1))

def sol():
    return [
        [3, 5, 6, 1, 2],
        [7, 1, 3, 2, 6],
        [9, 4, 7, 5, 1],
        [4, 5, 8, 3, 7]
    ]

# Check the result
print(sat(sol()))  # True

if __name__ == "__main__":
    assert sat(sol())

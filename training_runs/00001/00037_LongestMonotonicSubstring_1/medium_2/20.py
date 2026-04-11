def sat(x: Array[int, 2]):
    return all(x[i][j] <= x[i + 1][j] for i in range(len(x) - 1) for j in range(len(x[0])))

def sol():
    return [[-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1]]

# The function `sat` checks if all elements in the 2D array are in non-decreasing order.
# Therefore, the output of the function `sol` should be the same as the input `x`.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

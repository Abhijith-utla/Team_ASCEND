def sat(x: Array[int, 2]):
    return all(x[i][j] <= x[i + 1][j] for i in range(len(x) - 1) for j in range(len(x[0])))

def sol():
    return [[5, 7, 9, 11, 13, 15], [17, 19, 21, 23, 25, 27], [29, 31, 33, 35, 37, 39], [41, 43, 45, 47, 49, 51], [53, 55, 57, 59, 61, 63], [65, 67, 69, 71, 73, 75]]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

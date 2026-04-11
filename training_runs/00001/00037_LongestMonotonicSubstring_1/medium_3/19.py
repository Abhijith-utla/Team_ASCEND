def sat(x: List[List[int]]):
    return all(x[i][j] <= x[i + 1][j] for j in range(len(x[0])) for i in range(len(x) - 1))

def sol():
    return [int(i != len(x)-1) for x in [[3, 2, 1, 5, 4], [6, 7, 8, 9, 10]]]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(x):
    return all(x[i][j] <= x[i+1][j] for j in range(len(x[0])) for i in range(len(x)-1))

def sol():
    return all(x[i][j] <= x[i+1][j] for j in range(len(x[0])) for i in range(len(x)-1))

print(sat(sol()))  # Output: True

if __name__ == "__main__":
    assert sat(sol())

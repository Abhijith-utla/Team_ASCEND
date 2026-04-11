def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x) - 1)) and x[-1] >= x[-2]

def sol():
    return [3, 2, 1, 4]

if __name__ == "__main__":
    assert sat(sol())

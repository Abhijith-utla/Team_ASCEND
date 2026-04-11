def sat(x):
    return all(x[i] <= x[i+1] for i in range(len(x)))

def sol():
    return [1, 2, 3, 4, 5]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(x):
    return all(x[i] > x[i + 1] for i in range(len(x) - 1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())

def sat(x):
    return all(x[i] <= x[i + 1] for i in range(len(x))) if len(x) > 0 else False

def sol():
    return [i for i in range(10)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

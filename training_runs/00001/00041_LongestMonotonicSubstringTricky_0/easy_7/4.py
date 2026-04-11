def sat(x):
    return all(x[i] > x[i + 1] for i in range(len(x) - 1))

def sol():
    return [i for i in range(1, 21) if i % 2 == 0]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

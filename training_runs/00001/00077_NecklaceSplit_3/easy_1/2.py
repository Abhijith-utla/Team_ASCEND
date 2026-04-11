def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n)

def sol():
    return [['r' * n] * (2 * n) for n in range(len(lace) // 2)]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

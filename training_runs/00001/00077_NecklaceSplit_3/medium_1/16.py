def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n)

def sol():
    return ''

if __name__ == "__main__":
    assert sat(sol())

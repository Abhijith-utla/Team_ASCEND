def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n)

def sol():
    return ''

# Assertion is not necessary for this case as no answer is expected.

if __name__ == "__main__":
    assert sat(sol())

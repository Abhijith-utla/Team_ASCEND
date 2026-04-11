def sat(n: int, lace="bbbbrrbbrrbbrrbbrrbbb"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return 12

# Checker function
def check(n: int, lace="bbbbrrbbrrbbrrbbrrbbb"):
    return sat(n, lace)

assert check(sol())

if __name__ == "__main__":
    assert sat(sol())

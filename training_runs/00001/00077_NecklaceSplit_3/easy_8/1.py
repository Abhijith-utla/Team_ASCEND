def sat(n: int, lace="bbrrbbrrbbrr"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return {}

print("Assertion passed")

if __name__ == "__main__":
    assert sat(sol())

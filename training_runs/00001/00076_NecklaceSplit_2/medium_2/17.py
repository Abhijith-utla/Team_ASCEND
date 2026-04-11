def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    if n < 0:
        return False
    sub = lace[n: n + len(lace) // 2]
    return lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 4

# Assert statement
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

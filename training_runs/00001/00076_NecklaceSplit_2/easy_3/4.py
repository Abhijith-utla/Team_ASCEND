def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and len(lace) == 2 * len(sub) and lace.count("r") == 2 * sub.count("r") + 1 and lace.count("b") == 2 * sub.count("b")

def sol():
    return 1

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

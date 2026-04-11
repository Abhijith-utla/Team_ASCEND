def sat(n: int, lace="bbbbbbbbbbbbbbbbb"):
    sub = lace[n: n + len(lace) // 2 + 1]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return ""

assert sat(0)
assert not sat(1)
assert sat(10)
assert not sat(11)
assert sol() == ""

if __name__ == "__main__":
    assert sat(sol())

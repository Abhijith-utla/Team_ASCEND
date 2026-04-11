def sat(n: int, lace="bbbrrrbbbbrrrbbbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

assert sat(0)
assert not sat(1)
assert not sat(2)
assert not sat(3)
assert not sat(4)
assert not sat(5)

if __name__ == "__main__":
    assert sat(sol())

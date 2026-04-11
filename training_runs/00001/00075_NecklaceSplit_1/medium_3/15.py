def sat(n: int, m: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrrrbrrbrrbrbbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and m >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return ""

assert sat(0, 0)
assert not sat(1, 1)
assert not sat(2, 3)
assert not sat(4, 6)
assert sat(8, 12)
assert sat(16, 24)
assert not sat(32, 48)
assert not sat(64, 96)

if __name__ == "__main__":
    assert sat(sol())

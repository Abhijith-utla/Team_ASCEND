def sat(n: int, m: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrrrbrrbrrbrbbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and m >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

# Checker
assert sat(0, 0)
assert not sat(0, 1)
assert not sat(1, 0)
assert sat(1, 1)
assert not sat(2, 2)
assert not sat(3, 3)
assert not sat(4, 4)
assert not sat(5, 5)
assert sat(6, 6)
assert not sat(7, 7)
assert not sat(8, 8)
assert not sat(9, 9)
assert not sat(10, 10)
assert not sat(11, 11)
assert not sat(12, 12)
assert not sat(13, 13)
assert not sat(14, 14)
assert not sat(15, 15)
assert sat(16, 16)
assert not sat(17, 17)
assert not sat(18, 18)
assert not sat(19, 19)
assert not sat(20,

if __name__ == "__main__":
    assert sat(sol())

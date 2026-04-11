def sat(n: int, m: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrrrbrrbrrbrbbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and m >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

assert sat(0, 0)
assert not sat(0, 1)
assert not sat(1, 0)
assert not sat(1, 1)
assert sat(0, 2)
assert not sat(2, 3)
assert sat(3, 4)
assert not sat(4, 5)
assert sat(5, 6)
assert not sat(6, 7)
assert not sat(7, 8)
assert sat(8, 9)
assert not sat(9, 10)
assert sat(0, 11)
assert not sat(11, 12)
assert sat(12, 13)
assert not sat(13, 14)
assert sat(14, 15)
assert not sat(15, 16)
assert sat(16, 17)
assert not sat(17, 18)
assert sat(18, 19)
assert not sat(19, 20)
assert sat(0,

if __name__ == "__main__":
    assert sat(sol())

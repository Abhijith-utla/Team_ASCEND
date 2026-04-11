def sat(n: int, m: int, lace="rbbrrbbrbbrrbbrrbbrbrrrbbrbrrrrrrbbrrbrrbbrrbbbrbbrbbbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrrrrrrrrbrrrbrbbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and m >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

assert sat(0, 0)
assert not sat(1, 1)
assert sat(2, 3)
assert not sat(3, 5)
assert sat(4, 7)
assert not sat(5, 9)
assert sat(6, 11)
assert not sat(7, 13)
assert sat(8, 15)
assert not sat(9, 17)
assert sat(10, 19)
assert not sat(11, 21)
assert sat(12, 23)
assert not sat(13, 25)
assert sat(14, 27)
assert not sat(15, 29)
assert sat(16, 31)
assert not sat(17, 33)
assert sat(18, 35)
assert not sat(19, 37)
assert sat(20, 39)
assert not sat(21, 41)
assert sat(22, 43)

if __name__ == "__main__":
    assert sat(sol())

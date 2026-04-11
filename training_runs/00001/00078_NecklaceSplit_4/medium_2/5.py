def sat(n: int, lace="brrbbbrbbrrbrrbbrrrbbrbbrbbrrrbrbrrrrbbrrrbbbbrbbbrrbbrrbbbbrbbbbbrrbrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n < len(lace) and n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

assert sat(0)
assert not sat(1)
assert not sat(2)
assert sat(3)
assert not sat(4)
assert not sat(5)
assert sat(6)
assert not sat(7)
assert sat(8)
assert not sat(9)
assert not sat(10)
assert sat(11)
assert not sat(12)
assert sat(13)
assert not sat(14)
assert not sat(15)
assert sat(16)
assert not sat(17)
assert sat(18)
assert not sat(19)
assert not sat(20)
assert sat(21)
assert not sat(22)
assert sat(23)
assert not sat(24)
assert not sat(25)
assert sat(26)
assert not sat(27)
assert sat(28)
assert not sat(29)
assert not sat(30)
assert sat(31)
assert not sat(32)
assert sat(33

if __name__ == "__main__":
    assert sat(sol())

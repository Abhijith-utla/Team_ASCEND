def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

assert sat(0)
assert not sat(1)
assert not sat(2)
assert not sat(3)
assert sat(4)
assert not sat(5)
assert not sat(6)
assert not sat(7)
assert sat(8)
assert not sat(9)
assert not sat(10)
assert not sat(11)
assert sat(12)
assert not sat(13)
assert not sat(14)
assert not sat(15)
assert sat(16)
assert not sat(17)
assert not sat(18)
assert not sat(19)
assert sat(20)
assert not sat(21)
assert not sat(22)
assert not sat(23)
assert sat(24)
assert not sat(25)
assert not sat(26)
assert not sat(27)
assert sat(28)
assert not sat(29)
assert not sat(30)
assert not sat(31)
assert sat(32)
assert

if __name__ == "__main__":
    assert sat(sol())

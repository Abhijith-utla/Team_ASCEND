def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrbrrbrbbrbrrbbrrbrrbrrbrrbrbrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return ""

assert sat(0)
assert not sat(1)
assert not sat(2)
assert sat(3)
assert not sat(4)
assert sat(5)
assert not sat(6)
assert sat(7)
assert not sat(8)
assert sat(9)
assert not sat(10)
assert sat(11)
assert not sat(12)
assert sat(13)
assert not sat(14)
assert sat(15)
assert not sat(16)
assert sat(17)
assert not sat(18)
assert sat(19)
assert not sat(20)
assert sat(21)
assert not sat(22)
assert sat(23)
assert not sat(24)
assert sat(25)
assert not sat(26)
assert sat(27)
assert not sat(28)
assert sat(29)
assert not sat(30)
assert sat(31)
assert not sat(32)
assert sat(33)
assert not

if __name__ == "__main__":
    assert sat(sol())

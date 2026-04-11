def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrrrbrrbrrbrbbrrbbrrbrrbrrbrrrbbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("b") == 2 * sub.count("b") and lace.count("r") == 2 * sub.count("r")

def sol():
    return ""

assert sat(0)
assert not sat(1)
assert sat(2)
assert not sat(3)
assert sat(4)
assert not sat(5)
assert sat(6)
assert not sat(7)
assert sat(8)
assert not sat(9)
assert sat(10)
assert not sat(11)
assert sat(12)
assert not sat(13)
assert sat(14)
assert not sat(15)
assert sat(16)
assert not sat(17)
assert sat(18)
assert not sat(19)
assert sat(20)
assert not sat(21)
assert sat(22)
assert not sat(23)
assert sat(24)
assert not sat(25)

if __name__ == "__main__":
    assert sat(sol())

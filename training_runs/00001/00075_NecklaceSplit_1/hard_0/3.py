def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrbrrbrbbrbrrbbrrbrrbrrbrrbrbrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return "rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrrbrbbrbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"

# Testing
assert sat(0)
assert not sat(1)
assert not sat(2)
assert not sat(3)
assert not sat(4)
assert sat(5)
assert not sat(6)
assert not sat(7)
assert not sat(8)
assert not sat(9)
assert not sat(10)
assert sat(11)
assert not sat(12)
assert not sat(13)
assert not sat(14)
assert not sat(15)
assert not sat(16)
assert not sat(17)
assert not sat(18)
assert not sat(19)
assert not sat(20)
assert sat(2

if __name__ == "__main__":
    assert sat(sol())

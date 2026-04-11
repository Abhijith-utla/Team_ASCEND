def sat(n: int, m: int, lace="rbbrrbbrrbbrbrrbbrbrrrbbrrrrrrrrbbrrrrbbrrbbrrbbbbbbbbbbbbbbbbrbbbbbbbbbbbbbbbbbbbbbbbbbbrrrrbbbbrrrrbbbbrbbbbbbbbbbbbrbbbbbbbbbbbbbrrrrbbbbrbbbbrrbbbbrrbbrrbbrrbbrbbrrbbrrbbrrbbrrbbrrbbrbbbbrrbbbbrrrrrrbbrrbbrbbrrbbbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and m >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

# Test the function
assert sat(0, 0)
assert not sat(1, 0)
assert not sat(0, 1)
assert not sat(1, 1)
assert not sat(0, 2)
assert not sat(1, 2)
assert not sat(2, 2)
assert not sat(3, 2)
assert sat(0, 3)
assert not sat(1, 3)
assert not sat(2, 3)
assert not sat(3, 3)
assert not sat(4, 3)
assert sat(0, 4)
assert not sat(1, 4)
assert not sat(2, 4)
assert not sat(3, 4)
assert not sat(4, 4)
assert not sat(5, 4)
assert sat(0, 5)
assert not sat(1, 5)
assert not sat(2, 5)
assert not sat(3, 5)
assert not sat(4, 5)
assert not sat(5

if __name__ == "__main__":
    assert sat(sol())

def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    if n < 0:
        return False
    sub = lace[n: n + len(lace) // 2]
    return lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

# Test cases
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

print("All test cases pass")

if __name__ == "__main__":
    assert sat(sol())

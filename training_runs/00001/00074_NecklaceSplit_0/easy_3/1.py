def sat(n: int, lace="bbrbrbbrbrbrbbrb"):
    sub = lace[n: n + len(lace) // 4]
    return n >= 0 and lace.count("r") == sub.count("r") and lace.count("b") == sub.count("b")

def sol():
    return ""

# Testing
assert sat(0)
assert not sat(1)
assert sat(2)
assert not sat(3)
assert sat(4)
assert not sat(5)
assert sol()

if __name__ == "__main__":
    assert sat(sol())

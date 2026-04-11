def sat(n: int, lace="bbrbrbbrbrbrbbrb"):
    sub = lace[n: n + len(lace) // 3]
    return n >= 0 and lace.count("r") == sub.count("r") and lace.count("b") == sub.count("b")

def sol():
    return ""

assert sat()
assert not sat()
assert not sat(1)
assert sat(1, "bb")
assert not sat(1, "br")
assert not sat(1, "brb")
assert sat(1, "bbrbrb")
assert sat(2, "bb")
assert not sat(2, "br")
assert not sat(2, "brb")
assert sat(2, "bbrbrb")
assert not sat(10)
assert sat(10, "bbrbrbbrbrbrb")

if __name__ == "__main__":
    assert sat(sol())

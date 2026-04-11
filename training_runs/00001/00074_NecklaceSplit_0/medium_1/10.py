def sat(n: int, lace="bbrbrbbrbrbrbbrbrb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return ""

assert sat()
assert not sat()
assert not sat()
assert not sat()
assert sat("")
assert not sat("")
assert sat("brbrbrbrbr")
assert not sat("brbrbrbrbr")
assert not sat("brbrbrbrbrbrbrbrbrbrbrbrbrbr")
assert not sat("br")
assert not sat("brbrbrbrbrbr")
assert not sat("brbrbrbrbrbrbrbrbrbrbrbrbrbr")

if __name__ == "__main__":
    assert sat(sol())

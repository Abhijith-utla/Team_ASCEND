def sat(n: int, lace="bbrbrbbrbrbrbbrb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == sub.count("r") and lace.count("b") == sub.count("b")

def sol():
    return ""

# Checker
assert sat()

if __name__ == "__main__":
    assert sat(sol())

def sat(n: int, lace="bbrbrbbrbrbrbbrb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == sub.count("r") and lace.count("b") == sub.count("b")

def sol():
    return {"n": 0, "lace": "bbrbrbbrbrbrbbrb"}

assert sat(**sol())

if __name__ == "__main__":
    assert sat(sol())

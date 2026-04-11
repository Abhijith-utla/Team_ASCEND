def sat(n: int, lace="bbbbbbbbbbbbbbbbb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return ""

# Incorrect patterns
def sol(n):
    lace = "bbbbbbbbbbbbbbbbb"
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

# Correct patterns
def sol():
    return ""

def sol(n):
    lace = "bbbbbbbbbbbbbbbbb"
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

if __name__ == "__main__":
    assert sat(sol())

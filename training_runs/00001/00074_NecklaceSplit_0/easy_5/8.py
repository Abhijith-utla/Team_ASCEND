def sat(n: int, lace="bbbrrrbbbbrrrbbbbrr1"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

# checker
assert sat(0, "bbbrrrbbbbrrrbbbbrr1")
!pytest test_sat.py

if __name__ == "__main__":
    assert sat(sol())

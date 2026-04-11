def sat(n: int, lace="bbbrrrbbbbrrrbbbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n < 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 1

# Test case
assert sat(1, "bbbrrrbbbbrrrbbbbrr") == False
assert sat(2, "bbbrrrbbbbrrrbbbbrr") == True
assert sat(3, "bbbrrrbbbbrrrbbbbrr") == False
assert sat(4, "bbbrrrbbbbrrrbbbbrr") == True

if __name__ == "__main__":
    assert sat(sol())

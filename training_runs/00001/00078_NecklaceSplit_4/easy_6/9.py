def sat(n: int, lace="brrbbbrbbrrbrrbbrrrbbrbbrbbrrrbrbrrrrbbrrbbbbrbbbrrbbrrbbbbrbbbbbrrbrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n < len(lace) and n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b") and n + len(lace) // 2 < len(lace) # Added the condition

def sol():
    return 0

assert sat(0)

if __name__ == "__main__":
    assert sat(sol())

def sat(n: int, lace="brrbbbrbbrrbrrbbrrbrrrbbrbbrrrbbbrrrrrrbbrrbbrrrrbbrrbbrrrrrrbbbbrrrbbbbbbbbbbbrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n < len(lace) and n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

if __name__ == "__main__":
    assert sat(sol())

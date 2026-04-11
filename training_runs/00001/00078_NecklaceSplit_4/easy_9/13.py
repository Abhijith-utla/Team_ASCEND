def sat(n: int = 0):
    lace = "brrbbbrbbrrbrrbbrrbrrrbbrbbrrrbbbrrrrrrbbrrbbrrrrbbrrbbrrrrrrbbbbrrrbbbbbbbbbbbrrbbr"
    sub = lace[n: n + len(lace) // 2]
    return n < len(lace) and n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(n: int, m: int, lace="rbbrrbbrbbrrbbrrbbrbrrrbbrbrrrrrrbbrrbrrbbrrbbbrbbrbbbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrrrrrrrrbrrrbrbbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and m >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

assert sat(0, 0, lace="rbbrrbbrbbrrbbrrbbrbrrrbbrbrrrrrrbbrrbrrbbrrbbbrbbrbbbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrrbrrbrrbrrbrbbrbbbbbbrbbbrrrrrrrrbrrrbrbbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr")

if __name__ == "__main__":
    assert sat(sol())

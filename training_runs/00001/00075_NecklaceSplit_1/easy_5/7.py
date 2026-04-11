def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrrrbrrbrrbrbbrrbbrrbrrbrrbrrrbbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("b") == 2 * sub.count("r") and lace.count("r") == 2 * sub.count("b")

def sol():
    lace = "rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrrrbrrbrrbrbbrrbbrrbrrbrrbrrrbbrbbrrbbbbrrrrrbbrbrbrrbr"
    n = len(lace) // 2
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("b") == 2 * sub.count("r") and lace.count("r") == 2 * sub.count("b")

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrbrrrrbbrbbbrbrrbrbbrbrrbbbbrrrrrbrrrbbrrrrrrbrrrbrbbbrbbbrrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    lace = "bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrbrrrrbbrbbbrbrrbrbbrbrrbbbbrrrrrbrrrbbrrrrrrbrrrbrbbbrbbbbbbbrr"
    n = lace.find("r")
    if n == -1:
        return False
    else:
        sub = lace[n: n + len(lace) // 2]
        return n >= 0 and len(sub) == len(lace) // 2 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

print(sol())

if __name__ == "__main__":
    assert sat(sol())

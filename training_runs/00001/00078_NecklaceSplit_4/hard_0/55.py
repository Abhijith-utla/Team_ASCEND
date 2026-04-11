def sat(n: int, lace="brrbbbrbbrrbrrbbrrbrrrbbrbbrrrbrbrbrrrrbbrrrbrrbbbbrbbbrrbbrrrbbrbrbbbbbrrbrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return "brrbbbrbbrrbrrbbrrbrrrbbrbbrrrbrbrbrrrrbbrrrbbbbrbbbrrbbrrrbbrbbbbbrrbrrbbr"

# The function `sat` is already defined by the user.
# We don't need to define it here.

if __name__ == "__main__":
    assert sat(sol())

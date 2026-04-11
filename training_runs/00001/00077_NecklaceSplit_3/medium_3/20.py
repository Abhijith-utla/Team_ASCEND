def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrbrrrrbbrbbbbbrrrbrbbr"):
    return lace[n - 1:n + len(lace) // 2] == 'r' * (2 * (n - 1))

def sol():
    return "bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrrrrbbrbbbbbbbrrrbrbbr"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

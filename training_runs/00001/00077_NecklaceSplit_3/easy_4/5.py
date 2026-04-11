def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrrrrbbbbbbrbrrrrbbrbbbbbrrrbrbbr"):
    return lace[:len(lace) // 2] == 'r' * (2 * n)

def sol():
    return "brbrrbbrrbbbbrrbbrrrrbbbbbbbbbrrbbrrrrrrrbrbrbrbbbbbbbbbrrbbrbbrbrrbrrbbbrrrrrbbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrrrrrrbbbbbbrrrrbbrbbbbbbbrr"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

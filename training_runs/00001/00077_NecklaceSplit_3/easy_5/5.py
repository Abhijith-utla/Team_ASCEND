def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrrrrbbbbbbrbrrrrbbrbbbbbrrrbrbbr"):
    return lace[:len(lace) // 2] == 'rb' * (2 * n)

def sol():
    return 1

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

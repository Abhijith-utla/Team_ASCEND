def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrbrrrrbbrbbbrbrrbrbbrbrrbbbbrrrrrbrrrbbrrrrrrbrrrbrbbbrbbbrrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 1

print(sat(0))
!python
print(sat(1))
!python
print(sat(2))

if __name__ == "__main__":
    assert sat(sol())

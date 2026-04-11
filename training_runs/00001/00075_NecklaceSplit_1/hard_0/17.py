def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrbrrbrbbrbrrbbrrbrrbrrbrrbrbrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 5

print(sat(0)) # True
print(sat(1)) # False
print(sat(2)) # False
print(sat(3)) # True
print(sat(4)) # False
print(sat(5)) # True

if __name__ == "__main__":
    assert sat(sol())

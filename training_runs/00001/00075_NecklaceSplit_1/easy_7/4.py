def sat(n: int, m: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrrrrrrrrbrrbrbbrrbbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and m >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

print(sat(0, 0))
print(sat(0, 1))
print(sat(0, 2))
print(sat(0, 3))
print(sat(0, 4))
print(sat(0, 5))
print(sat(1, 1))
print(sat(1, 2))
print(sat(1, 3))
print(sat(1, 4))
print(sat(1, 5))
print(sat(2, 2))
print(sat(2, 3))
print(sat(2, 4))
print(sat(2, 5))
print(sat(3, 3))
print(sat(3, 4))
print(sat(3, 5))
print(sat(4, 4))
print(sat(4, 5))
print(sat(5, 5))

if __name__ == "__main__":
    assert sat(sol())

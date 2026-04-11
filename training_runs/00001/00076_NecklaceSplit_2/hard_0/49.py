def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

print(sat(0))
print(sat(1))
print(sat(2))
print(sat(3))
print(sat(4))
print(sat(5))

if __name__ == "__main__":
    assert sat(sol())

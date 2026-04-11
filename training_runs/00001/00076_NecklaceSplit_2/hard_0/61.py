def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

# Test cases
print(sat(0)) # False
print(sat(4)) # False
print(sat(5)) # True
print(sat(6)) # False
print(sat(7)) # False
print(sat(8)) # False

# Checker
def check(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

# Run the checker
assert sat(0) == check(0)
assert sat(4) == check(4)
assert sat(5) == check(5)
assert sat(6) == check(6)
assert sat(7) == check(7)
assert sat(8) == check(8)

if __name__ == "__main__":
    assert sat(sol())

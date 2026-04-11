def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    if n == 0:
        sub = lace[n: n + len(lace) // 2]
        return lace.count("r") == 2 * sub.count("r")
    elif n == 1:
        sub = lace[n: n + len(lace) // 2]
        return lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")
    elif n == 2:
        sub = lace[n: n + len(lace) // 2]
        return lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b") and n == len(lace) // 2

def sol():
    return ""

assert sat()
assert not sat()
assert not sat()
assert not sat()
assert not sat()
assert sat("brrrbrrbrbbbbbrrbbrr", 1)
assert not sat("brrrbrrbrbbbbbrrbbrr", 2)
assert not sat("brrrbrrbrbbbbbrrbbrr", 3)
assert not sat("brrrbrrbrbbbbbrrbbrr", 4)
assert not sat("brrrbrrbrbbbbbrrbbrr", 5)
assert sat("brrrbrrbrbbbbbrrbbrr", 6)

if __name__ == "__main__":
    assert sat(sol())

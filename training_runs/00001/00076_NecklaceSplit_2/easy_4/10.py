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
    return "brrrbrrbrbbbbbrrbbrr"

assert sat(0)
assert not sat(1)
assert not sat(2)
assert sat(2, "brrrbrrbrbbbbbrrbbrrbrrrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrr")
assert not sat(2, "brrrbrrbrbbbbbrrbbrrbrrrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrrbrr")

if __name__ == "__main__":
    assert sat(sol())

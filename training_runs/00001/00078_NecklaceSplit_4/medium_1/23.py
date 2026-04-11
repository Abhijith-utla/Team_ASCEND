def sat(n: int, lace="brrbbbrbbrrbrrbbrrbrrrbbrbbrrrbrbrbrrrrbbrrrbrrbbbbrbbbrrbbrrrbbrbrbbbbbrrbrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n < len(lace) and n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return 0

# If sat(sol()) returns True, this means sol() returns 0. If it returns False, this means there's an error in the solution.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

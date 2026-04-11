def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and len(lace) == 2 * len(sub) and lace.count("r") == 2 * sub.count("r") + 1 and lace.count("b") == 2 * sub.count("b")

def sol():
    return {}

# Incorrect cases
# For wrong lace
assert not sat(0, "brbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbrbr")
# For wrong lace length
assert not sat(0, "brrrbrrbrbbbbbrrbrrrbr")
# For wrong lace count of r and b
assert not sat(0, "brrrbrrrrbrrrbrrbrrbrr")
# For wrong lace count of r and b in middle of lace
assert not sat(1, "brrrbrrrrrbrrrbrrbrrbrr")
# For correct cases
assert sat(0, "brrrbrrbrbbbbbrrbrrr")
assert sat(1, "brrrbrrrrrbrrrbrrbrrbr")
assert sat(2, "brrrbrrrrrbrrrbrrbrrr")

if __name__ == "__main__":
    assert sat(sol())

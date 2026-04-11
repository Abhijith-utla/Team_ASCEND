def sat(n: int, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrbrrbrbbrbrrbbrrbrrbrrbrrbrbrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {"result": True}

# Test cases
assert sat(0, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrrrrbbrrrbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr")
assert not sat(0, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbrbbbrbrrrrbbrrrbrrbrrbrrbrrbrrrbbrbrbbrrbbbbrrrrrbbrbrbrrbr")
assert not sat(0, lace="rbbrrbbrbrbbbrrrbbrbrbrrbbrbbbbbbrrrrrrrrbrrrbbrbrrbbbrbbrrrbbrbbrrbrrbrbbrbbbbbbr

if __name__ == "__main__":
    assert sat(sol())

def sat(n: int, lace="bbbbbbbbbbbbbbbbb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return {"n": 0, "lace": "bbbbbbbbbbbbbbbbb"}

assert sat(0, "bbbbbbbbbbbbbbbbb")
assert not sat(1, "bbbbbbbbbbbbbbbbb")
assert not sat(2, "bbbbbbbbbbbbbbbbb")
assert not sat(3, "bbbbbbbbbbbbbbbbb")
assert sat(4, "bbbrrrbbbbbbbbbbb")
assert not sat(5, "bbbrrrbbbbbbbbbbb")
assert sat(6, "bbbrrrbbbbrrrbbbbb")
assert not sat(7, "bbbrrrbbbbrrrbbbbb")

if __name__ == "__main__":
    assert sat(sol())

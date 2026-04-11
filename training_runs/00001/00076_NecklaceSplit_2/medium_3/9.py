def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and len(sub) > 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

def sol():
    return { "n": 0, "lace": "brrrbrrbrbbbbbrrbbrr" }

assert sat(sol()["n"], lace=sol()["lace"])

if __name__ == "__main__":
    assert sat(sol())

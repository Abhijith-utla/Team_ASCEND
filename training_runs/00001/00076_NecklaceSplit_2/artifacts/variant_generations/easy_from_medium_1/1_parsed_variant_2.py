def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and len(lace) == 2 * len(sub) and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

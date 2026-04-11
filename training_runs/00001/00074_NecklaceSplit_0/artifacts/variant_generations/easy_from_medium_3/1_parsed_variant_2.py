def sat(n: int, lace="bbbbbbbbbbbbbbbbb"):
    sub = lace[n: n + len(lace) // 1]
    return n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b")

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

def sat(n: int, lace="brrrbrrbrbbbbbrrbbrr"):
    sub = lace[n: n + len(lace) // 2]
    return lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b") and n != len(lace) // 2

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

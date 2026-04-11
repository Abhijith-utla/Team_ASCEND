def sat(n: int, lace="bbrbrbbrbrbrbbrb"):
    sub = lace[n: n + len(lace) // 2]
    return n >= 0 and lace.count("r") == sub.count("r") and lace.count("b") == sub.count("b")

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

def sat(n: int, lace="brrbbbrbbrrbrrbbrrrbbrbbrbbrrrbrbrrrrbbrrbbbbrbbbrrbbrrbbbbrbbbbbrrbrrbbr"):
    sub = lace[n: n + len(lace) // 2]
    return n < len(lace) and n >= 0 and lace.count("r") == 2 * sub.count("r") and lace.count("b") == 2 * sub.count("b") # Removed the condition

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

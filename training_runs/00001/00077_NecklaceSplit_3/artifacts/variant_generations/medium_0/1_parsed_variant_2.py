def sat(n: int, lace="bbbbrrbbbbrrbbrrrbbrrbbrrrrrrrbrbrbbbrrbrrrbbbbbbbbbrbrbrbbbbbbbrrbbrbbrbrrbrbrrbbbrrrrrbrrbbrrrbbrbrrrbbbbrbbbrrrrbrbrrbbrbrbrbbrrbrrrbrbrrbbbbbbrbrrrrbbrbbbbbrrrbrbbr"):
    return lace[:len(lace) // 2] == 'r' * (2 * n)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

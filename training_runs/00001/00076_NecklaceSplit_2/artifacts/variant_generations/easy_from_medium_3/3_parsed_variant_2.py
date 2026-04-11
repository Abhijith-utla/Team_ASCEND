def sat(n: int):
    sub = 'brrrbrrbrbbbbbrrbbrr'[n: n + len('brrrbrrbrbbbbbrrbbrr') // 2]
    return n >= 0 and len(sub) > 0 and 'r' in lace and 'b' in lace and lace.count('r') == 2 * sub.count('r') and lace.count('b') == 2 * sub.count('b')

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

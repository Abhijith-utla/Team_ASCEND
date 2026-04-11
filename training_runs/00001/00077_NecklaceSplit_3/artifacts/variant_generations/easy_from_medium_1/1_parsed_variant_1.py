def sat(n: int):
    return lace[n:n + len(lace) // 2] == 'r' * (2 * n)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

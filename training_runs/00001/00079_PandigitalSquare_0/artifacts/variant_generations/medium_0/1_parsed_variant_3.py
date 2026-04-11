def sat(n: int):
    s = str(n * n)
    return len(s) == len(set(s))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

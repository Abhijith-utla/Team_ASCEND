def sat(n: int):
    s = str(n * n)
    return set(s) == set("0123456789")

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

def sat(n: int):
    s = str(n)
    return len(set(s)) == 10

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

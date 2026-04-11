def sat(n: int) -> bool:
    s = str(n)
    return len(s) == len(set(s))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

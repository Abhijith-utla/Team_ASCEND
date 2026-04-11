def sat(n: int) -> bool:
    s = str(n)
    return len(s) == len(set(s)) and s.isdigit()

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

def sat(s: str) -> bool:
    return len(s) == 10 and s.isalpha() and '0' not in s and '1' not in s

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

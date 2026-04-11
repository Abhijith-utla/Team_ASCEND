def sat(s: str) -> bool:
    if len(s) != 10 or not s.isalpha():
        return False
    return len(set(s)) == 5 and s[::2] == s[1::2]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

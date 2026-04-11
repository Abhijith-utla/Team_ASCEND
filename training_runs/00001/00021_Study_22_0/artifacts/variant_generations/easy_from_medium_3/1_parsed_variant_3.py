def sat(s: str) -> bool:
    if len(s) > 30 or len(s) < 5:
        return False
    return s.count(s[0]) == s.count(s[-1])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

def sat(s: str, t: str) -> bool:
    return sorted(s) == sorted(t) and s == t[::-1]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

def sat(s: str):
    return 'ooo' in s and 'o' not in s and s.count('o') == 1000

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

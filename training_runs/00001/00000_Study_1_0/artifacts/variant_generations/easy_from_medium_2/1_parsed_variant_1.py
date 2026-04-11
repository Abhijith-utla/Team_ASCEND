def sat(s: str):
    return 'o' in s and 'oo' not in s and s.count('o') == 1000

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

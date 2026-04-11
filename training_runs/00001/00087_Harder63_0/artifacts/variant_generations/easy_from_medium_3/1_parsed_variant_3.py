def sat(s: str):
    return len(set(s)) < 3 and s == '1-8*+/6'

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

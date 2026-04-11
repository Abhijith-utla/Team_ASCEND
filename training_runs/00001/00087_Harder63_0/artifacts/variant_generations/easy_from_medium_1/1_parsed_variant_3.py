def sat(s: str):
    return set(s) <= set("18-+*/321") and s.count("8") == 2 and s.count("1") == 1

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

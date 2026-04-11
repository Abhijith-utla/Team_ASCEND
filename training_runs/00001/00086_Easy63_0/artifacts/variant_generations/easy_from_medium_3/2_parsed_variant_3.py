def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 1 and s.count("1") == 4 and eval(s) == 18 * 1

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

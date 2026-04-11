def sat(s: str):
    return set(s) <= set("1-*") and s.count("8") == 4 and s.count("1") == 1 and eval(s) == 197

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")

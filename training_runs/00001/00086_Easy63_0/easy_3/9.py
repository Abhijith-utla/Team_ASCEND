def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 5 and s.count("1") == 0 and eval(s) == 98

def sol():
    return "18-+*/"

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return set(s) <= set("12345678+-*/") and s.count("8") == 4 and s.count("1") == 1 and eval(s) == 197

def sol():
    return "88888888+8-8*/"

if __name__ == "__main__":
    assert sat(sol())

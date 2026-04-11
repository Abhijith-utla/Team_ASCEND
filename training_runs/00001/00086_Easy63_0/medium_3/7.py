def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 5 and s.count("1") == 1 and eval(s) == 295

def sol():
    return "8"*5 + "-"*4 + "1"*1 + "+" + "8"*4

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 2 and s.count("1") == 3 and eval(s) == 18 * 2

def sol():
    return "8888"

if __name__ == "__main__":
    assert sat(sol())

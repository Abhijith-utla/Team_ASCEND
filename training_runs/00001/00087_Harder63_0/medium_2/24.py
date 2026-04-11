def sat(s: str):
    return set(s) <= set("1-8*+/3") and s.count("8") == 3 and s.count("1") == 1 and eval(s) == 63

def sol():
    return "1-8*+/3"

if __name__ == "__main__":
    assert sat(sol())

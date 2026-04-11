def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 3 and s.count("1") == 2 and eval(s) == 18 * 3

def sol():
    return "81818"

# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

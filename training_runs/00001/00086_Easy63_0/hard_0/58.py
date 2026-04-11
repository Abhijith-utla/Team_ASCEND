def sat(s: str):
    return set(s) <= set("18-+*/") and s.count("8") == 2 and s.count("1") == 1 and eval(s) == 63

def sol():
    return "81-*82/83-*84/85-*86/87-*88/89-*90"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

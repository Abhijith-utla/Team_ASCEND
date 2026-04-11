def sat(s: str):
    return set(s) <= set("18-+*/321") and s.count("8") == 3 and s.count("1") <= 1

def sol():
    return ""

if __name__ == "__main__":
    assert sat(sol())

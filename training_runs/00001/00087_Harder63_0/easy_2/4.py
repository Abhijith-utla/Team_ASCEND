def sat(s: str):
    return set(s) <= set("18-+*/321") and s.count("8") == 4 and s.count("1") == 1

def sol():
    return "1111"

if __name__ == "__main__":
    assert sat(sol())

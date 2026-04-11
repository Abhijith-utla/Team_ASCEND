def sat(s: str):
    return set(s) <= set("18-+*/321") and s.count("8") == 4 and s.count("1") == 1

def sol():
    return "81818181"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

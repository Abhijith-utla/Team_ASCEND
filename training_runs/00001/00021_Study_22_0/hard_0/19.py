def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    return "insufficient data" if len(set(input())) != 5 else "valid"

if __name__ == "__main__":
    assert sat(sol())

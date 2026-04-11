def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return "181818181818181818"

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

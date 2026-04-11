def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    s = "8181818181818181818181"
    return s

if __name__ == "__main__":
    assert sat(sol())

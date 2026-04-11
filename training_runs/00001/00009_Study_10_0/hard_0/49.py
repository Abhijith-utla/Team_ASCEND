def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return "84138181847141818184484"

if __name__ == "__main__":
    assert sat(sol())

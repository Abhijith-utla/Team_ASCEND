def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    s = ''.join(str(8 ** 1818))
    return s == s[::-1] and len(s) > 11

print(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    binary = bin(8 ** 1818)[2:]
    return binary == binary[::-1] and len(binary) > 11

if __name__ == "__main__":
    assert sat(sol())

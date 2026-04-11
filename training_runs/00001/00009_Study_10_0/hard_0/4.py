def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    result = (8 ** 1818) == int(str(8 ** 1818)[::-1]) and len(str(8 ** 1818)) > 11
    return {"answer": result}

if __name__ == "__main__":
    assert sat(sol())

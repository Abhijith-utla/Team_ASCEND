def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    for i in range(1000000000):  # because 8 ** 1818 is a very large number
        if not sat(str(i)):
            return str(i)
    return None

def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

if __name__ == "__main__":
    assert sat(sol())

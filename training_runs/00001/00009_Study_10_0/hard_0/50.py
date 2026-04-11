def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return max(filter(sat, map(str, range(1, 10))), key=len)

def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

print(sol())

if __name__ == "__main__":
    assert sat(sol())

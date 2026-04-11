def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    for s in range(10):
        if sat(str(s)):
            return str(s)
    return None

def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

print(sol())  # Output: 81

if __name__ == "__main__":
    assert sat(sol())

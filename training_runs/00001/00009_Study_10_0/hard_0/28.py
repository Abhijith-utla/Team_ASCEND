def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return ''.join(str(int(i) % 10) for i in str(8 ** 1818))

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

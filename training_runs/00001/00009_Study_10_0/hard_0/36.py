def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return ''.join(ch for ch in str(8 ** 1818) if ch == ch[::-1])

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

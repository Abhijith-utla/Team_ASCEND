def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    s = "8123456789012345678"  # Assuming the required string is the reverse of "8" repeated 1818 times.
    return s

# Checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

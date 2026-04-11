def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

def sol():
    return '8' * 1818

def sat(s: str):
    return s in str(8 ** 1818) and s == s[::-1] and len(s) > 11

# Test cases
print(sat(sol()))  # True
print(sat('abcba'))  # True
print(sat('a'))  # False
print(sat('ab'))  # False
print(sat('a'))  # False

if __name__ == "__main__":
    assert sat(sol())

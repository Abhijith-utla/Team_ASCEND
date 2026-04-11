def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    s = 'oo' * 1000 + 'o'
    return s

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

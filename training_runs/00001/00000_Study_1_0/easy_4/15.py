def sat(s: str):
    return 'o' in s and 'oo' not in s and s.count('o') == 1000

def sol():
    s = 'oo' * 1000
    return s

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

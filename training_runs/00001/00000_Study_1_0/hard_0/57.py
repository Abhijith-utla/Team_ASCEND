def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

def sol():
    s = 'oo' * 1000
    return s

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

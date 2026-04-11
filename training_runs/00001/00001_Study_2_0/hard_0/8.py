def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = 'ooo' * 1000 + 'hooooooooo'
    return s.count('ooo') == 1000 and s.count('oo') == 100 and s.count('o') == 801

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

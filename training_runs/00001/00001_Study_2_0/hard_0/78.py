def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = 'oo' * 1000 + 'h' * 801
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

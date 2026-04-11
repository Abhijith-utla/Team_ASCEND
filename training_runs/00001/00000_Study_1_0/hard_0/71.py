def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

def sol():
    s = 'oooooooooooooooooooooooo'
    return s

# Test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

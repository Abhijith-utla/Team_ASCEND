def sat(s: str):
    return s.count('x') == 100 and s.count('xo') == 101 and s.count('xx') == 98

def sol():
    return 'x' * 100 + 'o' * 101 + 'x' * 98

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

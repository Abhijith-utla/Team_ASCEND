def sat(s: str):
    return s.count('x') == 100 and s.count('xo') == 101 and s.count('xx') == 98

def sol():
    s = 'xxooo' * 100 + 'x' + 'xxooo' * 101
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

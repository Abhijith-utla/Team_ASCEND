def sat(s: str):
    return s.count('x') == 100 and s.count('xo') == 101 and s.count('xx') == 98

def sol():
    s = 'xxxxxxxxxxo' * 101 + 'x'
    return s.count('x') == 100 and s.count('xo') == 101 and s.count('xx') == 98

if __name__ == "__main__":
    assert sat(sol())

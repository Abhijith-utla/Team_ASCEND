def sat(s: str):
    return s.count('x') == 100 and s.count('o') == 101 and s.count('xx') == 98

def sol():
    s = 'ooo'*100 + 'x' + 'ooo'*98
    return s.count('x') == 100 and s.count('o') == 101 and s.count('xx') == 98

if __name__ == "__main__":
    assert sat(sol())

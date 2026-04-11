def sat(s: str):
    return s.count('x') == 110 and s.count('o') == 101 and s.count('xx') == 98

def sol():
    s = 'xxxxxxxxxxxxxxxxxxxxxxxxxooo'
    return s

if __name__ == "__main__":
    assert sat(sol())

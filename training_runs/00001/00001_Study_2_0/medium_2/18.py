def sat(s: str):
    return s.count('y') == 100 and s.count('yo') == 101 and s.count('yy') == 98

def sol():
    s = 'y'*100 + 'yo'*101 + 'yy'*98
    return s

if __name__ == "__main__":
    assert sat(sol())

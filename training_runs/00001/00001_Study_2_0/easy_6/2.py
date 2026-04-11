def sat(s: str):
    return s.count('yy') == 100 and s.count('yo') == 101 and s.count('y') == 98

def sol():
    s = 'y' * 98 + 'yo' * 101 + 'yy' * 100
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

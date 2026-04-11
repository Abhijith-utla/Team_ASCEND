def sat(s: str):
    return s.count('yy') == 100 and s.count('y') == 101 and s.count('yo') == 98

def sol():
    return 'yyyyyyyyyyy'

if __name__ == "__main__":
    assert sat(sol())

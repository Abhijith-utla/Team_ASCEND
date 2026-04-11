def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 0

def sol():
    s = 'oooooooooooooooooooooooooo'
    return s.count('o') == 1000 and s.count('oo') == 0

if __name__ == "__main__":
    assert sat(sol())

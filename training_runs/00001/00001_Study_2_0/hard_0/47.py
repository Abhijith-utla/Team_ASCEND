def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = 'hoooooooooooooooooooooooooo'
    return s.count('oo') == 100 and s.count('oooo') == 1000 and s.count('o') == 800

if __name__ == "__main__":
    assert sat(sol())

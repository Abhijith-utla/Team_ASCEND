def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = 'hoooooooo' * 1000
    return s.count('ooo') == 100 and s.count('oo') == 1000 and s.count('o') == 801

if __name__ == "__main__":
    assert sat(sol())

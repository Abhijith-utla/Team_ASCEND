def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    return 'o' * 1000 + 'oo' * 100 + 'ho' * 801

if __name__ == "__main__":
    assert sat(sol())

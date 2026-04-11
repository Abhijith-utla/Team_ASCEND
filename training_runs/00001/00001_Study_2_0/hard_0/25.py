def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = 'ho' * 1000 + 'o' * 100 + 'ho'
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

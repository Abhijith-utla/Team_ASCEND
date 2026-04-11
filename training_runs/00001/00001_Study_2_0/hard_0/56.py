def sat(s: str):
    return s.count('o') == 1000 and s.count('oo') == 100 and s.count('ho') == 801

def sol():
    s = "ooooooooooooooooooooho"
    return s.count('o'), s.count('oo'), s.count('ho')

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    s = 'oooooooooooooooooooooo'
    return s

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

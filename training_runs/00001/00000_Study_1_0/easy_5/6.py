def sat(s: str):
    return s.count('oo') >= 2

def sol():
    return 'oooo' if sat('oooo') else 'not oo'

if __name__ == "__main__":
    assert sat(sol())

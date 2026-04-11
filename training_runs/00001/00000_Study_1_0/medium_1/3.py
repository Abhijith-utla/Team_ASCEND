def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'oooooooooooo' and 'oo' in 'oooooooooooo'

if __name__ == "__main__":
    assert sat(sol())

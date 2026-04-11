def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'oooooooooooooooooooo' and 'oo' * 1000 in 'oooooooooooooooooooo'

if __name__ == "__main__":
    assert sat(sol())

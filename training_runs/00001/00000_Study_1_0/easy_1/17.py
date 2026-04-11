def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'oooooooooo' and 'o' * 1000 in 'oooooooooo'

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'ooooooooooooooooooooo' and 'oo' in 'ooooooooooooooooooooo'

if __name__ == "__main__":
    assert sat(sol())

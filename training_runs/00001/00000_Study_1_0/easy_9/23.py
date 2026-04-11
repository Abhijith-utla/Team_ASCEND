def sat(s: str):
    return 'ooo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'ooo' not in 'ooooooooooooooooooo' and 'o' in 'ooooooooooooooooooo' and 'o' not in 'ooooooooooooooooooo'

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'ooo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'ooo' not in 'ooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo' and 'o' in 'oooooooooo'

if __name__ == "__main__":
    assert sat(sol())

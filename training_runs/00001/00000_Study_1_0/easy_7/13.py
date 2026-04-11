def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'oo' not in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooooooo

if __name__ == "__main__":
    assert sat(sol())

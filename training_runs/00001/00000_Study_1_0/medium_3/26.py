def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'oo' not in 'oooooooooooo' and 'o' in 'oooooooooooo' and 'o' not in 'oooooooooooo' and 1000 == sum([i for i in 'oooooooooooo' if i == 'o'])

if __name__ == "__main__":
    assert sat(sol())

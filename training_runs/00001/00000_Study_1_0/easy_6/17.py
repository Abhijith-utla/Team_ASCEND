def sat(s: str):
    return 'ooo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'ooo' in 'oooooooooo' and 'o' not in 'oooooooooo' and 'oooooooooo'.count('o') == 1000

if __name__ == "__main__":
    assert sat(sol())

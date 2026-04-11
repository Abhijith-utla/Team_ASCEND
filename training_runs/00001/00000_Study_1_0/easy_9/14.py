def sat(s: str):
    return 'ooo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'ooo' not in 'oooooooooooo' and 'o' in 'oooooooooooo' and 'oooooooooooo'.count('o') == 1000

if __name__ == "__main__":
    assert sat(sol())

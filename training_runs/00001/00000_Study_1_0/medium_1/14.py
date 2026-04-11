def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'oooooooooooo' and 'o' in 'oooooooooooo' and 1000 == 'oooooooooooo'.count('o')

if __name__ == "__main__":
    assert sat(sol())

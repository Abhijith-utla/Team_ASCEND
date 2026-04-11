def sat(s: str):
    return 'oo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'oo' in 'a' * 1000 and 'o' not in 'a' * 1000 and 'a' * 1000.count('o') == 1000

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'oo' in s and s.count('o') >= 1000

def sol():
    return 'oo' in '1234567890' * 1000 and '1234567890' * 1000.count('o') >= 1000

if __name__ == "__main__":
    assert sat(sol())

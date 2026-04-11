def sat(s: str):
    return 'ooo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'ooo' in 'ooo' and 'o' not in 'ooo' and 'ooo'.count('o') == 1000

if __name__ == "__main__":
    assert sat(sol())

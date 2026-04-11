def sat(s: str):
    return 'oo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'oo' in 'Hello World' and 'o' not in 'Hello World' and 'Hello World'.count('o') == 1000

if __name__ == "__main__":
    assert sat(sol())

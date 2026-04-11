def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'oo' not in 'This is a test string. The string should contain exactly 1000 "o" characters.' and 'o' in 'This is a test string. The string should contain exactly 1000 "o" characters.' and 'o' in 'This is a test string. The string should contain exactly 1000 "o" characters.'

if __name__ == "__main__":
    assert sat(sol())

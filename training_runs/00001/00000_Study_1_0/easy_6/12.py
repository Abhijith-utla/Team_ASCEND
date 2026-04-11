def sat(s: str):
    return 'ooo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'ooo' in 'This is a string with exactly 1000 o's' and 'o' not in 'This is a string with exactly 1000 o's' and 'o' not in 'This is a string with exactly 1000 o's' and 'o' not in 'This is a string with exactly 1000 o's'

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'oo' in s and s.count('o') <= 1000

def sol():
    return 'oo' in 'Your long string here' and 'Your long string here'.count('o') <= 1000

if __name__ == "__main__":
    assert sat(sol())

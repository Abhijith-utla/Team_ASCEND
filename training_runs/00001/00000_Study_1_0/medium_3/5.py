def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return {'answer': 'oo not in s and o in s and s.count('o') == 1000'}

if __name__ == "__main__":
    assert sat(sol())

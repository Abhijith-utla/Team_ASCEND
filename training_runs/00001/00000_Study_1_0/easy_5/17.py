def sat(s: str):
    return 'oo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'oo' in 'oooooooooooo' and 'o' not in 'oooooooooooo' and 'oooooooooooo'.count('o') == 1000

print(sol())

if __name__ == "__main__":
    assert sat(sol())

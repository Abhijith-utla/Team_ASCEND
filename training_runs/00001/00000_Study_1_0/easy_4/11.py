def sat(s: str):
    return 'o' in s and 'oo' not in s and s.count('o') == 1000

def sol():
    s = 'oooooooooooo'
    return sat(s)

print(sol())  # False

if __name__ == "__main__":
    assert sat(sol())

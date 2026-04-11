def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'oo' not in 'oooooooooooooooooooooo' and 'o' in 'oooooooooooooooooooooo' and 'oooooooooooooooooooooo'.count('o') == 1000

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

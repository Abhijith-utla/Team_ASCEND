def sat(s: str):
    return 'ooo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'ooo' in 'oooooooooooooooooooooooo' and 'o' not in 'oooooooooooooooooooooooo' and 'oooooooooooooooooooooooo'.count('o') == 1000

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'oo' not in 'oooooooooo' and 'o' in 'oooooooooo' and 'oooooooooo'.count('o') == 1000

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in 'oooooooooooooooooooooooooo' and 'oo' in 'oooooooooooooooooooooooooo'

# Run the checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return 'oo' not in s and 'o' in s and s.count('o') == 1000

def sol():
    return 'oo' not in 'oooooooooooooo' and 'o' in 'oooooooooooooo' and 'oooooooooooooo'.count('o') == 1000

# Check the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

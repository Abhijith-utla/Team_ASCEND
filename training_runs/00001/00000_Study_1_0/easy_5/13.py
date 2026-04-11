def sat(s: str):
    return 'oo' in s and 'o' not in s and s.count('o') == 1000

def sol():
    return 'oo' in 'Hello, World!' and 'o' not in 'Hello, World!' and 'H' in 'Hello, World!'*1000

# For the checker to run, the function must return True when called
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

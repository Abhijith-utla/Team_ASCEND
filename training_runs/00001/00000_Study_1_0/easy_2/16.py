def sat(s: str):
    return 'oo' in s and s.count('o') >= 1000

def sol():
    return 'oo' in 'Hello World' and 'Hello World'.count('o') >= 1000

# Test the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

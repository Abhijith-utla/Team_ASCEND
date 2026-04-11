def sat(s: str):
    return s.count('oo') >= 2

def sol():
    return 'oo' in 'oooo'

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

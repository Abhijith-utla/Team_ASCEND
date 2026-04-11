def sat(s: str):
    return 'oo' in s and s.count('o') == 1000

def sol():
    return 'oo' in '000000000000000000000000' and '000000000000000000000000' == '000000000000000000000000'

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

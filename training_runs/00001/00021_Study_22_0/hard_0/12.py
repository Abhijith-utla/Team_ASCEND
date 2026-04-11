def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    s = 'abcd1234'
    return s[::2] in s and len(set(s)) == 5

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    return s[::2] in s and len(set(s)) == 5

def sol():
    s = 'abcde'
    return s[::2]

# Test the function
assert sat(sol()) == 'ace'

if __name__ == "__main__":
    assert sat(sol())

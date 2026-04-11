def sat(s: str):
    return len(s) == 1000 and 'o' in s

def sol():
    s = 'Hello, world!'
    return s

# Do not modify the code below this line
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

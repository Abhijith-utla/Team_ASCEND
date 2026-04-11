def sat(n: int):
    s = set(str(n))
    return s == {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def sol():
    return 0

# Test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

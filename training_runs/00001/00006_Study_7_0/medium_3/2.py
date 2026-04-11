def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    s = '8' * (8 ** 2888) ** 0.5
    return s.count('8') > 8 and len(s) == 3

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

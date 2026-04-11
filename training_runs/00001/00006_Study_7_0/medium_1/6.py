def sat(s: str):
    return str(int(8 ** 2888)).count(s) > 8 and len(s) == 3

def sol():
    s = str(int(8 ** 2888))
    return str(int(8 ** 2888)).count(s) > 8 and len(s) == 3

# Test case
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

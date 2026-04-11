def sat(n: int):
    s = str(n * n)
    return len(set(s)) == 10

def sol():
    return 1234567890

# Do not remove this assert statement
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

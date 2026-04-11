def sat(n: int, m: int):
    assert n >= 0, 'n must be greater than or equal to 0'
    assert m >= 0, 'm must be greater than or equal to 0'
    assert n + m >= 0, 'Sum of n and m must be greater than or equal to 0'
    return n + m >= 0

def sol():
    return 0

# Run the checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

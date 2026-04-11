def sat(x: float):
    return x - 3.1415 == 123.456789

def sol():
    return 123.456789

# To check the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(x: float):
    return x - 3.1415 == 123.456000001

def sol():
    return 123.456000001

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

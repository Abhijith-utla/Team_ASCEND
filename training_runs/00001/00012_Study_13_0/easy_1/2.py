def sat(x: float):
    return x - 3.1415 == 123.456

def sol():
    return 123.456

# The checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(x: float):
    return x < 3.1416

def sol():
    return 1.23456789

if __name__ == "__main__":
    assert sat(sol())

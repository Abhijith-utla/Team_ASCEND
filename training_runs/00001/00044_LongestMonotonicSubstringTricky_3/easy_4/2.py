def sat(x: int, y: int) -> bool:
    return x <= y

def sol():
    return 10, 20

assert sat(*sol())

if __name__ == "__main__":
    assert sat(sol())

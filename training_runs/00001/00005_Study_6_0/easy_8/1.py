def sat(n: int):
    return n % 2 == 0

def sol():
    return 0 if sat(0) else 1

if __name__ == "__main__":
    assert sat(sol())

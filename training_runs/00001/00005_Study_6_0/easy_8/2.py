def sat(n: int):
    return n % 2 == 0

def sol():
    return (lambda n: n % 2 == 0)(10)

if __name__ == "__main__":
    assert sat(sol())

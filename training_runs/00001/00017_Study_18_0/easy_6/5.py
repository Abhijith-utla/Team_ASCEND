def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

def sol():
    a = 10
    b = 22.3456789123456789
    return sat(a, b)

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

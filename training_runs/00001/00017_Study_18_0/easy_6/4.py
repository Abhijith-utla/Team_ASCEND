def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

def sol():
    import math
    a = 10
    b = 20.0
    return sat(a, b)

def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    assert sat(sol())

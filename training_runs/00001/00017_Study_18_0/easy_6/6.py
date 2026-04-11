def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

def sol():
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if sat(a, b):
                return a, b
    return None

def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    assert sat(sol())

def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

def sol():
    return 5, 12

# Run the assert statement
assert sat(*sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(a: int, b: float) -> bool:
    return a - b == math.sqrt(a**2 + b**2)

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

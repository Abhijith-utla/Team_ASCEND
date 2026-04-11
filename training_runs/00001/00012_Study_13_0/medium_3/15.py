def sat(x: float):
    return str(x - 3.1417).startswith("123.456")

def sol():
    return "123.456"

assert sat(float(sol()))

if __name__ == "__main__":
    assert sat(sol())

def sat(x: float):
    return str(x - 3.1418).startswith("123.456")

def sol():
    x = 3.1418
    return str(x - 0.000001).startswith("123.456")

if __name__ == "__main__":
    assert sat(sol())

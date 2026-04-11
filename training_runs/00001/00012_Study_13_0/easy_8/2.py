def sat(x: float):
    return str(x - 3.1417).startswith("123.4567")

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

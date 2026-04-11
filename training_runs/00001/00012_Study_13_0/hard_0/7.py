def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

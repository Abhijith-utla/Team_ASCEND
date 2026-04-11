def sat(i: int):
    return i > 0 and i % 2 == 0

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

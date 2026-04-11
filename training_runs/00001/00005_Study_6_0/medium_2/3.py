def sat(i: int):
    return i % 5 == 0 and i < 100

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

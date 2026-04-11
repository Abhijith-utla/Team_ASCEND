def sat(i: int) -> bool:
    return i % 2 == 0

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

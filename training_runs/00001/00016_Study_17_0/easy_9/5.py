def sat(i: int) -> bool:
    return i < (i + 1)

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

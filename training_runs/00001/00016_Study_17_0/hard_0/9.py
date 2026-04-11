def sat(i: int):
    return len(str(i + 1000)) > len(str(i + 1001))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

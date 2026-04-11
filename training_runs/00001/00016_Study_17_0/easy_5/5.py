def sat(i: int) -> bool:
    return len(str(i + 10)) == len(str(i + 100))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

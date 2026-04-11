def sat(s: str) -> bool:
    return s == 'abc4.5' or s == 'abc4.56'

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

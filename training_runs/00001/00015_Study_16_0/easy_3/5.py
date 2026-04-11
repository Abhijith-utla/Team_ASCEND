def sat(s: str) -> bool:
    return s == '5.5'

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

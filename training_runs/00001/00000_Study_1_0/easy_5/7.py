def sat(s: str):
    return s.count('oo') >= 2

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

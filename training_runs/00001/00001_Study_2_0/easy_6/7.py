def sat(s: str):
    return s.count('yy') == 100 and s.count('yo') == 101 and s.count('y') == 98

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

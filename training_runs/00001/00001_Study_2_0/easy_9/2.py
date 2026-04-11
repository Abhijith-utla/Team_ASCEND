def sat(s: str):
    return s.count('m') == 400 and s.count('mm') == 401 and s.count('mmm') == 398

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

def sat(s: str):
    if s.count('oo') != 0:
        return False
    return True

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

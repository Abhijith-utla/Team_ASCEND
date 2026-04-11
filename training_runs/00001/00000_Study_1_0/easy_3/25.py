def sat(s: str):
    return 'oo' in s and s.count('o') <= 1000

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

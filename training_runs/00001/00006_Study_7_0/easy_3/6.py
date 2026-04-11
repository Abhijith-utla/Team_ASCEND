def sat(s: str):
    return str(int(8 ** 2888)).count(s) == 10 and len(s) == 3

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

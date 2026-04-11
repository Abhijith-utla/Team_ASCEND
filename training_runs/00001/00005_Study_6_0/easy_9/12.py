def sat(n: int):
    return n <= 10 ** 10 and n % 2 == 0

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

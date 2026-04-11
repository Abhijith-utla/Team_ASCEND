def sat(s: str) -> bool:
    return str(2888 ** int(8)).count(s) > 8 and len(s) == 3

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

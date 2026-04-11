def sat(s: str):
    return len(s) == 1000 and 'o' in s

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

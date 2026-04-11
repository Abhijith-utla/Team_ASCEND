def sat(quine: str):
    return eval(quine) == quine

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

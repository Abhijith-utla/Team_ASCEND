def sat(li: List[int]):
    return set(li) == {0}

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

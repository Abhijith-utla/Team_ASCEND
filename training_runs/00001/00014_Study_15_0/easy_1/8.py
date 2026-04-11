def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** x) - 1 for x in li)

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

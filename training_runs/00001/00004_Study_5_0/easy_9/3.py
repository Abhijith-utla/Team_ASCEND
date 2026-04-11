def sat(li: list) -> bool:
    return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

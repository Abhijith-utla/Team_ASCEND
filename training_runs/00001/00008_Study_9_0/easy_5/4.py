def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

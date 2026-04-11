def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

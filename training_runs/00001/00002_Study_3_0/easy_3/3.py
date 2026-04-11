def sat(li: List[int]):
    return sorted(li) == list(range(998)) and all(li[i] != i for i in range(998)) and len(li) == 999

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

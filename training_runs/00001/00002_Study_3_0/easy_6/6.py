def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(999)) and all(li[i] == i for i in range(len(li)))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

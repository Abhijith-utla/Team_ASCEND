def sat(li: List[int]) -> bool:
    return len(li) == len(set(li))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

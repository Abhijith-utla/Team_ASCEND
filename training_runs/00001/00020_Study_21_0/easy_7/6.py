def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)])

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all([i <= j for i in li for j in li if i > j])

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

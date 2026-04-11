def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(20))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

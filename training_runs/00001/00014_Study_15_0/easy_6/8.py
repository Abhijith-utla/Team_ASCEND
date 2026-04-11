def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    for x in range(20):
        if not (x + y == 2 ** x for y in li[:x]):
            return False
    return True

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

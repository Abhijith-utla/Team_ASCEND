def sat(li: List[int]):
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

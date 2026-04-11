def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return li[li[0]] == li[li[1]] and li[li[2]] != li[li[3]]

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

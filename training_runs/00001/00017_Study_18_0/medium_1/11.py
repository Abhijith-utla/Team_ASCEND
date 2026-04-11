def sat(ls: List[str]) -> bool:
    return all(s not in ls for s in ls)

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

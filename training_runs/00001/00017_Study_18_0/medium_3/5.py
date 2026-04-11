def sat(ls: List[str]) -> bool:
    return len(ls) == len(set(ls))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

def sat(ls: List[str]):
    return min(ls) == max(ls) == str(len(ls))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

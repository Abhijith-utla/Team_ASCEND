def sat(ls: List[str]):
    return "".join(ls) == str(7 ** 64.5) and all(len(s) == 8 for s in ls)

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

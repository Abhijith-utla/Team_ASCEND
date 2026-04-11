def sat(ls: List[str]):
    return tuple(ls) in zip('dee', 'doo', 'dah!')

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

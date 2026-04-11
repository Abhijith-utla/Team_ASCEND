def sat(li: List[int]):
    return [chr(i) for i in li] == list("Hello World".replace(" ", ""))

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

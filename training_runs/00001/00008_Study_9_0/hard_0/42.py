def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    raise RuntimeError("No parseable sol() extracted")


if __name__ == "__main__":
    assert sat(sol())

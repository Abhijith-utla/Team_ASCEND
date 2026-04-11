def sat(li: List[int]):
    return [chr(i) for i in li] == list(
        "The quick brown fox jumps over the lazy dog".replace(" ", ""))

def sol():
    def sat(li: List[int]):
        return [chr(i) for i in li] == list(
            "The quick brown fox jumps over the lazy dog".replace(" ", ""))

    return sat

if __name__ == "__main__":
    assert sat(sol())

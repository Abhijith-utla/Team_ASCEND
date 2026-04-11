def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    def sat(li: List[int]):
        return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
            "The five boxing wizards jump quickly")

    def gen():
        return [ord(c) for c in "The quick brown fox jumps over the lazy dog"]

    return [gen(), sat(gen())]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

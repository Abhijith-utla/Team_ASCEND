def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    def check_word(word):
        return all(word[i] == "The quick brown fox jumps over the lazy dog"[i] for i in range(len(word)))

    return [check_word(word) for word in "The five boxing wizards jump quickly".split()]

if __name__ == "__main__":
    assert sat(sol())

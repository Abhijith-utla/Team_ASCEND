def sat(li: List[int]):
    return ["The quick brown fox jumps over the lazy dog"[i] for i in li] == list(
        "The five boxing wizards jump quickly")

def sol():
    li = [ord(i) for i in "The quick brown fox jumps over the lazy dog"]
    assert sat(li)
    return {"answer": "The quick brown fox jumps over the lazy dog"}

# This is a test assert for the function. It will fail if the function is not correct.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

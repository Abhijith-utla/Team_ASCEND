def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

def sol():
    return [ord(i) for i in "The five boxing wizards jump quickly"] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

# Testing
assert sat([ord(i) for i in "The five boxing wizards jump quickly"]) == [104, 105, 115, 32, 119, 101, 32, 105, 115, 116, 101, 114, 115, 32, 112, 111, 115, 105, 116, 105, 111, 110]

if __name__ == "__main__":
    assert sat(sol())

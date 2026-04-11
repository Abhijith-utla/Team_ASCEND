def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

def sol():
    def sat(li: List[int]):
        return [ord(i) for i in li] == list("The five boxing wizards jump quickly".replace(" ", ""))

    return sat

if __name__ == "__main__":
    assert sat(sol())

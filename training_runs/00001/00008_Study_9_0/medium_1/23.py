def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

def sol():
    li = [ord(i) for i in list("The five boxing wizards jump quickly")]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())

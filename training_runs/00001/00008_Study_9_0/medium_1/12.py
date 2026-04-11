def sat(li: List[int]):
    return [ord(i) for i in li] == list(
        "The five boxing wizards jump quickly".replace(" ", ""))

def sol(li: List[int]):
    return [ord(i) for i in li] == list("The five boxing wizards jump quickly".replace(" ", ""))

# Test the function
assert sol([ord(i) for i in 'The five boxing wizards jump quickly'.replace(' ', '')])

if __name__ == "__main__":
    assert sat(sol())

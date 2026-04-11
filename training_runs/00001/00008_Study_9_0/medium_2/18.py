def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

def sol(li: List[int]) -> List[int]:
    return [i for i in li if i >= 0]

if __name__ == "__main__":
    assert sat(sol())

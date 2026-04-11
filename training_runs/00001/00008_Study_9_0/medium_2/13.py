def sat(li: List[int]):
    return [i for i in li if i >= 0] == list(
        "The five boxing wizards jump quickly".split(" "))

def sol():
    return [i for i in range(10)]

# test case
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

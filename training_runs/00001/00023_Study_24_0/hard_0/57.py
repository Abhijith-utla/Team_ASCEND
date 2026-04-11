def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    li = [1, 3, 2, 3, 1, 3, 2, 3, 1, 17]
    return li

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

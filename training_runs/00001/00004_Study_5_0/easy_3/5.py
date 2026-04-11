def sat(li: List[int]):
    return li.count(1) == 1 and li.count(2) == 1 and li.count(3) == 1 and li.count(4) == 1 and li.count(5) == 1 and li.count(6) == 1 and li.count(7) == 1 and li.count(8) == 1 and li.count(9) == 1

def sol():
    return 5

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return li.count(1) == 10 and li.count(2) == 10 and li.count(3) == 10 and li.count(4) == 10 and li.count(5) == 10 and li.count(6) == 10 and li.count(7) == 10 and li.count(8) == 10 and li.count(9) == 10

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return li.count(17) == 0 or li.count(3) == 0

def sol():
    return [1, 2, 3, 17, 4, 5, 6]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

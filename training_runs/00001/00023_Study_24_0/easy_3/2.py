def sat(li: List[int]):
    return li.count(17) == 0 or li.count(3) == 0

def sol():
    return [17, 3] if 17 in [17, 3] else [3, 17]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

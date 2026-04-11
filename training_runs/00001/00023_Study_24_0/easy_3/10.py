def sat(li: List[int]):
    return li.count(17) == 0 or li.count(3) == 0

def sol():
    return [17 if i == 17 else 3 for i in [17, 17, 3, 3, 3] if i == 17 or i == 3]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

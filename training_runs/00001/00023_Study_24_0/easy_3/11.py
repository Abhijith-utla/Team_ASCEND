def sat(li: List[int]):
    return li.count(17) == 0 or li.count(3) == 0

def sol():
    li = [1, 2, 3, 17, 4, 5]
    return li

if __name__ == "__main__":
    assert sat(sol())

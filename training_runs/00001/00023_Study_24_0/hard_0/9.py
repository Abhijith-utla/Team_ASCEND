def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

def sol():
    import random
    li = [random.randint(0, 1) for _ in range(10)]
    while not sat(li):
        li = [random.randint(0, 1) for _ in range(10)]
    return li

def sat(li: List[int]):
    return li.count(17) == 3 and li.count(3) >= 2

print(sol())

if __name__ == "__main__":
    assert sat(sol())

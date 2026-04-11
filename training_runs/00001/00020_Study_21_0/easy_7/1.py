def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)])

def sol():
    li = [random.randint(1, 10) for _ in range(8)]
    while not sat(li):
        li = [random.randint(1, 10) for _ in range(8)]
    return li

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)])

if __name__ == "__main__":
    assert sat(sol())

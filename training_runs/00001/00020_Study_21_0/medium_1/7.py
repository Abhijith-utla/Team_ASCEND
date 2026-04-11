def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    from random import randint
    li = [randint(1, 10) for _ in range(10)]
    while not sat(li):
        li[randint(0, 9)] = randint(1, 10)
    return li

if __name__ == "__main__":
    assert sat(sol())

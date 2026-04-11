def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    from random import shuffle
    li = [i for i in range(10)]
    shuffle(li)
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

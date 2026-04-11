def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(10)]) and len(set(li)) == 3

def sol():
    li = [1, 2, 3]
    while not sat(li):
        li = [1, 2, 3]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

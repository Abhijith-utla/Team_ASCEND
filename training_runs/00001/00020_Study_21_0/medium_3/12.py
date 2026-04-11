def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

def sol() -> List[int]:
    li = [1, 2, 2, 3, 3, 3, 4]
    while not sat(li):
        li[li.index(4) - 1] += 1
        li[li.index(4) + 1] += 1
    return li

def sat(li: List[int]) -> bool:
    return all([li[i] != li[i + 1] for i in range(7)]) and len(set(li)) == 3

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol() -> List[int]:
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        if sat(li):
            return li
        li[li.index(min(li)) + 1] += 1
        if li[li.index(max(li)) - 1] + 1 == li[li.index(max(li))]:
            li[li.index(max(li)) - 1] += 1

def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

if __name__ == "__main__":
    assert sat(sol())

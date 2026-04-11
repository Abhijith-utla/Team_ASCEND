def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    li: List[int] = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

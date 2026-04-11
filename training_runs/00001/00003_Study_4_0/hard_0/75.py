def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    li = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
    return li

if __name__ == "__main__":
    assert sat(sol())

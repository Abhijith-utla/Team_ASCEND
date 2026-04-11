def sat(li: List[int]):
    return len(li) == 10 and li.count(li[3]) == 2

def sol():
    return [4, 3, 7, 2, 4, 5, 7, 8, 6, 1]

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
    return li

if __name__ == "__main__":
    assert sat(sol())

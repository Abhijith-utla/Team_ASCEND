def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

def sol():
    li = [i for i in range(1, 11)] + [13]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: list) -> bool:
    return all(li.count(i) == i for i in range(10)) and li.count(0) == 1

def sol():
    li = [0]*10
    return li

if __name__ == "__main__":
    assert sat(sol())

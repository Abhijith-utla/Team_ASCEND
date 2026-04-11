def sat(li: List[int]):
    return li.count(17) == 1 and li.count(3) == 1

def sol():
    li = [1, 3, 17, 3, 17, 1, 3]
    return li.count(17) == 1 and li.count(3) == 1

print(sol())

if __name__ == "__main__":
    assert sat(sol())

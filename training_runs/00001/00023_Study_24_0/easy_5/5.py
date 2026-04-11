def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    li = [17, 3, 17, 17, 3, 17, 17, 17]
    return li.count(17) == 2 and li.count(3) == 1

print(sol())

if __name__ == "__main__":
    assert sat(sol())

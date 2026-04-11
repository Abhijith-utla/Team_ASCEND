def sat(li: List[int]):
    return li.count(17) == 1 and li.count(3) == 1

def sol():
    return [17] if 17 not in [17, 3] else [3]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

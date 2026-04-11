def sat(li: List[int]):
    return li.count(17) == 1

def sol():
    return 17 in [17, 13, 21, 14, 56, 89, 17]

if __name__ == "__main__":
    assert sat(sol())

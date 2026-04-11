def sat(li: List[int]):
    return li.count(3) == 2

def sol():
    return [3] * 2

if __name__ == "__main__":
    assert sat(sol())

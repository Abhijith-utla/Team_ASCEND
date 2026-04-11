def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    return [i for i in range(1, 11) if sum([li.count(i) for li in range(1, 11)]) != i]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

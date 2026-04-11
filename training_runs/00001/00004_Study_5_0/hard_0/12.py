def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    return [i for i in range(10) if 10 <= sum([li.count(i) for li in [list(range(10)) for _ in range(5)]])]

if __name__ == "__main__":
    assert sat(sol())

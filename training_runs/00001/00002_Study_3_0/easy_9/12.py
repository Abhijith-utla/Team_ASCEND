def sat(li: List[int]):
    return sorted(li) == list(range(1001))

def sol():
    return sorted([x for x in range(1, 1001)])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

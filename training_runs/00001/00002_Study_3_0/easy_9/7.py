def sat(li: List[int]):
    return sorted(li) == list(range(1001))

def sol():
    return sorted([i for i in range(1, 1001)])

def sat(li: List[int]):
    return sorted(li) == list(range(1001))

if __name__ == "__main__":
    assert sat(sol())

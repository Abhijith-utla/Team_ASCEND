def sat(li: List[int]):
    return sorted(li) == list(range(1001))

def sol():
    return sorted(range(1, 1001))

if __name__ == "__main__":
    assert sat(sol())

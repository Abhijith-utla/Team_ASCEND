def sat(li: List[int]):
    return sorted(li) == list(range(999))

def sol():
    return sorted([1, 2, 3]) == list(range(999))

if __name__ == "__main__":
    assert sat(sol())

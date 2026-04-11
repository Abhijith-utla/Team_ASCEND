def sat(li: List[int]):
    return sorted(li) == list(range(999))

def sol():
    return sorted([i for i in range(999)])

if __name__ == "__main__":
    assert sat(sol())

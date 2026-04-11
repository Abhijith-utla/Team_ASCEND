def sat(li: List[int]):
    return sorted(li) == list(range(1000))

def sol():
    return sorted(list(range(1000)))

if __name__ == "__main__":
    assert sat(sol())

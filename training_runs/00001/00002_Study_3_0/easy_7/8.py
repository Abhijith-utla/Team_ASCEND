def sat(li: List[int]):
    return sorted(li) == list(range(999))

def sol():
    return [i+1 for i in range(998)] + [999]

if __name__ == "__main__":
    assert sat(sol())

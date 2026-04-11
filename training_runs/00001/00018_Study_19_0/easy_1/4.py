def sat(li: List[int]):
    return len(li) == 30

def sol():
    return [1]*30

if __name__ == "__main__":
    assert sat(sol())

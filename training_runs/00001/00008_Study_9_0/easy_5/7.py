def sat(li: List[int]):
    return len(li) == 10 and max(li) == 12

def sol():
    return [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

if __name__ == "__main__":
    assert sat(sol())

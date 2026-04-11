def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li[3] != li[3]:
        return False
    return True

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":
    assert sat(sol())

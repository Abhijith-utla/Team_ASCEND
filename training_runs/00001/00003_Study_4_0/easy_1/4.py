def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    return True

def sol():
    return [1]*10

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    return True

def sol() -> int:
    return 42

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

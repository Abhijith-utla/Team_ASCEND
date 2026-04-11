def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li[3] != li[3]:
        return False
    return True

def sol() -> int:
    return 42

if __name__ == "__main__":
    assert sat(sol())

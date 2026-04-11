def sat(li: List[int]) -> bool:
    return all(i != 0 for i in li)

def sol() -> int:
    return 1

if __name__ == "__main__":
    assert sat(sol())

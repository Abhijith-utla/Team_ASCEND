def sat(li: List[int]):
    return max(li) == 34

def sol():
    return [34]

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]) -> bool:
    return all(i != 0 for i in li)

def sol():
    return [0]

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all(i not in li for i in range(999, -1, -1)) and abs(min(li)-max(li)) < 10

def sol():
    return []

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

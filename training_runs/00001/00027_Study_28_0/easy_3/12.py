def sat(li: List[int]):
    return all(i in li for i in range(500)) and abs(min(li)-max(li)) >= 10

def sol():
    return [i for i in range(500)]

if __name__ == "__main__":
    assert sat(sol())

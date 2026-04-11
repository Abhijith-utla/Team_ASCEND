def sat(li: List[int]):
    return all(i in li for i in range(500)) and abs(min(li)-max(li)) >= 10

def sol():
    li = [i for i in range(500)]
    return li

if __name__ == "__main__":
    assert sat(sol())

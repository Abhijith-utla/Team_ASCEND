def sat(li: List[int]):
    return all(i in li for i in range(500)) and abs(min(li)-max(li)) >= 10

def sol():
    import random
    li = [random.randint(1, 500) for _ in range(500)]
    assert sat(li)
    return li

if __name__ == "__main__":
    assert sat(sol())

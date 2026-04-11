def sat(li: List[int]):
    return all(i in li for i in range(500)) and abs(min(li)-max(li)) >= 10

def sol():
    import random
    li = [random.randint(-500, 500) for _ in range(1000)]
    return li

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

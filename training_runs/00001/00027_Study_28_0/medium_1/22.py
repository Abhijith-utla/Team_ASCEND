def sat(li: List[int]):
    return all(i not in li for i in range(1000)) and abs(min(li)-max(li)) < 10

def sol():
    import random
    li = [random.randint(-500, 500) for _ in range(1000)]
    while not sat(li):
        li = [random.randint(-500, 500) for _ in range(1000)]
    return li

print(sat(sol()))  # This will print whether the function 'sat' is correct

if __name__ == "__main__":
    assert sat(sol())

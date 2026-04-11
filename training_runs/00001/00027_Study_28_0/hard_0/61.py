def sat(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

def sol():
    li = [i for i in range(100) if i not in [4, 16, 20, 25, 30, 32, 34, 38, 40, 42]] + [1000 - 99 for _ in range(99)]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())

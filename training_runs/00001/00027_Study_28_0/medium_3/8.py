def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li if i != j) and len(li) == 100

def sol():
    li = [i for i in range(100)]
    return li

if __name__ == "__main__":
    assert sat(sol())

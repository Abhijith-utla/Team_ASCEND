def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li) and len(set(li)) == 10

def sol():
    li = [i for i in range(10)]
    while not sat(li):
        li = [i for i in range(10)]
    return li

if __name__ == "__main__":
    assert sat(sol())

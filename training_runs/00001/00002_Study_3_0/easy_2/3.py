def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(999)) and len(li) == 1000

def sol():
    li = [0] * 1000
    li[0] = 1
    return li

if __name__ == "__main__":
    assert sat(sol())

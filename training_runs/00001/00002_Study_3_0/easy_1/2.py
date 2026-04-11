def sat(li: List[int]):
    return sorted(li) == list(range(len(li))) and all(li[i] != i for i in range(len(li))) and len(li) == 1000

def sol():
    li = [i for i in range(1000)]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

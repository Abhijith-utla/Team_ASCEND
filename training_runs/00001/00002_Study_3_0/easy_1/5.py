def sat(li: List[int]):
    return sorted(li) == list(range(len(li))) and all(li[i] != i for i in range(len(li))) and len(li) == 1000

def sol():
    import random
    li = [random.randint(0, 1000) for _ in range(1000)]
    return sat(li)

def sat(li: List[int]):
    return sorted(li) == list(range(len(li))) and all(li[i] != i for i in range(len(li))) and len(li) == 1000

if __name__ == "__main__":
    assert sat(sol())

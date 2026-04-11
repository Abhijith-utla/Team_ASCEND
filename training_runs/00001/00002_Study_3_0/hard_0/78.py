def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    li = [i % 1000 for i in range(999)] + [999]
    random.shuffle(li)
    return sorted(li)

def sat(li):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

if __name__ == "__main__":
    assert sat(sol())

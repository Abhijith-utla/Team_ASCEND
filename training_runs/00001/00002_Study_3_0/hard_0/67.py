def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol():
    li = [i+1 for i in range(998)]
    li.append(0)
    assert sat(li)
    return li

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return sorted(li) == list(range(998)) and all(li[i] != i for i in range(998)) and len(li) == 999

def sol():
    li = [i for i in range(998)]
    li.remove(499)
    return li

if __name__ == "__main__":
    assert sat(sol())

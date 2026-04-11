def sat(li: List[int]):
    return sorted(li) == list(range(998)) and all(li[i] != i for i in range(998)) and len(li) == 999

def sol():
    li = list(range(998))
    li.append(999)
    li[998] = 999
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

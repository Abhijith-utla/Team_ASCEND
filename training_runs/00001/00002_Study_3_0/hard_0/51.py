def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol(li: List[int]):
    li = sorted(li)
    for i in range(len(li)):
        if li[i] != i:
            return i
    return len(li)

def sat(li: List[int]):
    return sol(li) == 999

if __name__ == "__main__":
    assert sat(sol())

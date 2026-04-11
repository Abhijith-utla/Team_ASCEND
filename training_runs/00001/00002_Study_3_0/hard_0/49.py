def sat(li: List[int]):
    return sorted(li) == list(range(999)) and all(li[i] != i for i in range(len(li)))

def sol() -> List[int]:
    li = [i for i in range(999)]
    li[0] = 0
    return li

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]) -> bool:
    return sorted(li) == list(range(len(li))) and all(li[i] == i for i in range(len(li)))

def sol(li: List[int]) -> bool:
    sorted_li = sorted(li)
    return sorted_li == list(range(len(li))) and all(li[i] == i for i in range(len(li)))

if __name__ == "__main__":
    assert sat(sol())

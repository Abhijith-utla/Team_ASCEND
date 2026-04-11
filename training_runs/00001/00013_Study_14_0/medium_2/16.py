def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol():
    return sat([5, 3, 2, 1, 4])

def sat(li: List[int]):
    return all([i < sum(li[:j]) + li[j] for j in range(len(li)) for i in range(j+1)])

if __name__ == "__main__":
    assert sat(sol())

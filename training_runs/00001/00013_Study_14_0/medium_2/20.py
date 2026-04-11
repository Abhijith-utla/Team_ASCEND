def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol(li: List[int]):
    for x in set(li):
        if li.index(x) < sum(li[:li.index(x)]):
            return False
    return True

if __name__ == "__main__":
    assert sat(sol())

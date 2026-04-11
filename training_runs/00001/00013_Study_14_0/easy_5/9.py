def sat(li: List[int]):
    return all((li.index(x) < sum(li[:li.index(x)])) for x in set(li))

def sol():
    return sat([1, 2, 3, 4, 5])

def sat(li: List[int]):
    return all((li.index(x) < sum(li[:li.index(x)])) for x in set(li))

print(sat([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    assert sat(sol())

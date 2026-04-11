def sat(li: List[int]):
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

def sol():
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

if __name__ == "__main__":
    assert sat(sol())

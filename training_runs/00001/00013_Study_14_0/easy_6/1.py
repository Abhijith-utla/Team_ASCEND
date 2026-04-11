def sat(li: List[int]):
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

def sol():
    li = [1, 2, 3, 4, 5]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())

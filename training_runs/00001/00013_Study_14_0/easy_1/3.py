def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

def sol():
    li = [3, 2, 1, 4, 5]
    return sat(li)

def sat(li: List[int]):
    return all(li[i] < sum(li[:i]) for i in range(1, len(li)))

if __name__ == "__main__":
    assert sat(sol())

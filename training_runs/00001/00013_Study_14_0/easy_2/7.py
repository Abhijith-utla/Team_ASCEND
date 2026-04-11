def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

def sol():
    return sat([5, 3, 2, 1, 6])

def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

if __name__ == "__main__":
    assert sat(sol())

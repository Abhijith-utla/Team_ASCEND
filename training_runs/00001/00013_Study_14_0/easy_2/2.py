def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

def sol():
    return sat([1, 2, 3, 4, 5])

def sat(li: List[int]):
    return all(li[i] < sum(li[:i+1]) for i in range(len(li)))

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all([i < sum(li[:i]) for i in range(20)])

def sol():
    li = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())

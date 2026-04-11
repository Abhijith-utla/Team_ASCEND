def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(5)])

def sol():
    return [1, 2, 3, 4, 5] if sat([1, 2, 3, 4, 5]) else [6, 7, 8, 9, 10]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

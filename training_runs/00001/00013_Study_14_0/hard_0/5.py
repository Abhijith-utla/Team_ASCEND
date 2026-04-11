def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    li = [int(x) for x in input().split()]
    return sat(li)

def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

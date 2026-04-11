def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    li = [i for i in range(20)]
    return sat(li)

def sat(li: List[int]):
    for x in range(20):
        for y in li[:x]:
            if x + y != 2 ** x:
                return False
    return True

if __name__ == "__main__":
    assert sat(sol())

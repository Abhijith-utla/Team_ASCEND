def sat(li: List[int]):
    for x in range(20):
        if not (x + y == 2 ** x for y in li[:x]):
            return False
    return True

def sol():
    li = [1] * 20
    return li

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    li = [1]*20
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

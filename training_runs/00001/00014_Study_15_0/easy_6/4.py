def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

def sol():
    return 2 ** 20 - 1

if __name__ == "__main__":
    assert sat(sol())

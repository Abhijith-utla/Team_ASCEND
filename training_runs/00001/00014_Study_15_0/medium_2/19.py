def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    return 2 ** 18

def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

# test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

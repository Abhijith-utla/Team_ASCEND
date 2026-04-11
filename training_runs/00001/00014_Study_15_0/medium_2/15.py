def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    return [i for i in range(20) if all(x + y == 2 ** x for x in range(i + 1) for y in range(i + 1))]

if __name__ == "__main__":
    assert sat(sol())

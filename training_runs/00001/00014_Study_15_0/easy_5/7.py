def sat(li: List[int]):
    for x in range(20):
        if not (x + y == 2 ** x for y in li[:x]):
            return False
    return True

def sol():
    return [i for i in range(20) if all(i + j == 2 ** j for j in range(i + 1))]

if __name__ == "__main__":
    assert sat(sol())

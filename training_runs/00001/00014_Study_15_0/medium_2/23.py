def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x])

def sol():
    def sat(li: List[int]):
        return all(x + y == 2 ** x for x in range(20) for y in li[:x])

    return sat([])

if __name__ == "__main__":
    assert sat(sol())

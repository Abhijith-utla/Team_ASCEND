def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

def sol():
    return [x for x in range(20) if (2 ** x) - 1 != (2 ** (x + 1)) - 1]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

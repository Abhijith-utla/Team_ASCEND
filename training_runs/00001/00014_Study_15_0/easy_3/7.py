def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

def sol():
    return [x for x in range(10) if not sat([x])]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all(x == i for i, x in enumerate(li))

def sol():
    return [i for i, x in enumerate(li) if x != i]

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

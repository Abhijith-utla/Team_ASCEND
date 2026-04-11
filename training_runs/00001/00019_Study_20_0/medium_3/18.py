def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    return [3, 6, 9]

# Checker will run:
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

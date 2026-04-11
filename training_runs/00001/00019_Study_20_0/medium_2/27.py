def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    return [1, 2, 3, 4]

# Calling the assert statement with the solution function as the argument
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

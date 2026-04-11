def sat(li: List[int]) -> bool:
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    return [3] * 10

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

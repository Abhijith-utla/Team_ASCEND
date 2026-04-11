def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    return sum([i**2 for i in range(1, 11)])

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

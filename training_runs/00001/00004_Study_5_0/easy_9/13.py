def sat(li: list) -> bool:
    return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

def sol():
    return [i for i in range(10) if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

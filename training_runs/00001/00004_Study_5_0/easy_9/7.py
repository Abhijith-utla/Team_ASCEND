def sat(li: list) -> bool:
    return all([li.count(i) == i for i in range(10)]) == li.count(0) == 1

def sol():
    return all([[i for i in range(10)]*100 for _ in range(10)])

# test case
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

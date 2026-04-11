def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    li = [1, 2, 3, 4, 5]
    return li

# checker function
def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

# execute the checker
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

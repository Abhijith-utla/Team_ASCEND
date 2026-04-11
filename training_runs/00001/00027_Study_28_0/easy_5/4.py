def sat(li: List[int]):
    return all(i - j == 10 for i in li for j in li)

def sol():
    return [10]*10

# Checker code
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

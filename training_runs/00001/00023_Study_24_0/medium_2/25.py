def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    return [17, 3] if sat([17, 3, 17, 17]) else [3, 3]

# To check the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

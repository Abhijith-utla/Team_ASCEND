def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 0

def sol():
    return [17, 3]

# test the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

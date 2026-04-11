def sat(li: List[int]):
    return li.count(17) == 2 and li.count(3) == 1

def sol():
    return [17, 3, 17, 3]

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

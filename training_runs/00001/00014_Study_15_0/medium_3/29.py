def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(20))

def sol():
    return [sum(li[:i]) for i in range(20)]

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

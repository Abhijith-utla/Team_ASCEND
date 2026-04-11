def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(20))

def sol():
    return sum(i for i in range(20) if sum(range(i)) == sum(range(i, 20)))

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

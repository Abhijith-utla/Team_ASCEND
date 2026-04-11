def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(20))

def sol():
    return 12

if __name__ == "__main__":
    assert sat(sol())

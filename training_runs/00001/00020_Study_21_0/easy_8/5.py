def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(6)])

def sol():
    return 0

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

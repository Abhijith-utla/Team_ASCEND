def sat(li: List[int]):
    return all([i < sum(li[:i]) for i in range(20)])

def sol():
    li = [1]*20
    assert sat(li)
    li = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert not sat(li)

if __name__ == "__main__":
    sol()

if __name__ == "__main__":
    assert sat(sol())

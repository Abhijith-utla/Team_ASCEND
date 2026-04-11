def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(1, 11)])

    assert sat([1]*10)
    assert not sat([2]*10)
    assert sat([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    assert not sat([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert sat([1, 1, 2, 2, 2, 3, 3, 3, 4, 4])
    assert not sat([1, 2, 3, 4, 4, 4, 5, 5, 5, 5])
    print("All tests passed.")

sol()

if __name__ == "__main__":
    assert sat(sol())

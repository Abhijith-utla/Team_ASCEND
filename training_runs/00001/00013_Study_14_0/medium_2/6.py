def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol():
    def sat(li: List[int]):
        for i in set(li):
            if li.index(i) < sum(li[:li.index(i)]):
                return False
        return True

    assert sat([1, 2, 3, 2, 3, 4, 5])
    assert not sat([1, 2, 3, 2, 3, 5, 5])

sol()

if __name__ == "__main__":
    assert sat(sol())

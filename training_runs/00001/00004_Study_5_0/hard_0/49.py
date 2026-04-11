def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    def sat(li: List[int]):
        return all([li.count(i) == i for i in range(10)])

    assert sat([])
    assert sat([1, 1, 1, 2, 2, 2, 3, 3, 3, 4])
    assert not sat([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4])
    assert not sat([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
    return None

# Run the test case
print(sol())

if __name__ == "__main__":
    assert sat(sol())

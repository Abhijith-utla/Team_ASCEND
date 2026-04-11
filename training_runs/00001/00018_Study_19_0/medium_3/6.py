def sat(li: List[int]):
    return set(li) == {0}

def sol():
    return 0

# Testing
def test_sat():
    assert sat([])
    assert not sat([0])
    assert not sat([1])
    assert sat([0, 0])
    assert not sat([0, 1])
    assert not sat([1, 0])
    assert not sat([-1, 1])
    assert not sat([1, -1])
    assert sat([1, 1, 1])

test_sat()

if __name__ == "__main__":
    assert sat(sol())

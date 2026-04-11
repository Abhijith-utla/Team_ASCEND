def sat(li: List[int]):
    return all((j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])))

def sol():
    return {0}

# Let's test it
def test_sat():
    assert sat([1, 2, 3, 4, 5])
    assert not sat([1, 2, 4, 4, 5])
    assert sat([1, 2, 4, 6, 5])
    assert not sat([1, 2, 4, 7, 5])
    assert sat([0])
    assert not sat([1, 2, 4, 9, 5])
    assert not sat([2, 3, 4, 6, 5])
    print("All tests passed!")

test_sat()

if __name__ == "__main__":
    assert sat(sol())

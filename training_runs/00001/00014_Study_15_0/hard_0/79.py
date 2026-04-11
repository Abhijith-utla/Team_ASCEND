def sat(li: List[int]):
    return all(sum(li[:i]) == 2 ** i - 1 for i in range(20))

def sol():
    return sum([(2 ** i) - 1 for i in range(20)])

# Test the function
def test_sat():
    assert sat(list(range(19)))
    assert not sat(list(range(1, 19)))
    assert sat(list(range(2 ** 19)))
    assert not sat(list(range(2 ** 19, 2 ** 20)))

test_sat()

if __name__ == "__main__":
    assert sat(sol())

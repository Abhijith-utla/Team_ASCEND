def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    return [i for i in range(10) if i not in [li.count(i) for li in [i for i in range(10)]]]

# Let's test our solution
def test_sol():
    assert sat(sol())

if __name__ == "__main__":
    test_sol()

if __name__ == "__main__":
    assert sat(sol())

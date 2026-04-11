def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    li = [i for i in range(10)]
    return sat(li)

# Testing
def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())

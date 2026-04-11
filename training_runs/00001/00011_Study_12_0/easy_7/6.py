def sat(li: List[int]):
    li.insert(0, 4)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    li = [0]*1000 + [4] + [0]*1000
    return li

# Test the solution
def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())

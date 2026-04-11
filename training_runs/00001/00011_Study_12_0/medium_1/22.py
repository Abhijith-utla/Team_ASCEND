def sat(li: List[int]):
    return all(i + j == 1 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return { 'li': [4]*1000 }

# Test
def test_sol():
    assert sat(sol()['li'])

# Run Test
test_sol()

if __name__ == "__main__":
    assert sat(sol())

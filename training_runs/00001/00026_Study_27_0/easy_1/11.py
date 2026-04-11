def sat(li):
    return li[li[0]] == li[li[1]]

def sol():
    return [2, 3, 4, 5, 6, 7]

def test_sol():
    assert sat(sol())

test_sol()

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    li = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def test_sat():
    assert sat(sol())

test_sat()

if __name__ == "__main__":
    assert sat(sol())

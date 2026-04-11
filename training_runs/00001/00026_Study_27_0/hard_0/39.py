def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    li = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

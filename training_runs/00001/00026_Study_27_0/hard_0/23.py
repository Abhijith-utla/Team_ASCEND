def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    return [1, 0, 0, 1, 1, 0, 1, 0, 0, 0]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

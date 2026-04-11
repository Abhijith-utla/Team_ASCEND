def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    return [4, 2, 3, 7]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    li = [2, 0, 2, 3, 1]
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

if __name__ == "__main__":
    assert sat(sol())

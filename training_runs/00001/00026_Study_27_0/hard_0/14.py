def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    return [2, 1, 3, 5, 4]

if __name__ == "__main__":
    assert sat(sol())

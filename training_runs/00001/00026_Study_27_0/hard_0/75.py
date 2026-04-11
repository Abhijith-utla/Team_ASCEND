def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    li = [3, 2, 0, 1]
    li[li[0]] = 6
    li[li[1]] = 5
    li[li[li[0]]] = 4
    li[li[li[1]]] = 3
    li[li[li[0]]] = 2
    li[li[li[1]]] = 1
    return li

if __name__ == "__main__":
    assert sat(sol())

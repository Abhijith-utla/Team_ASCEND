def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return li[li[0]] != li[li[1]] and li[li[li[0]]]] == li[li[li[1]]]]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

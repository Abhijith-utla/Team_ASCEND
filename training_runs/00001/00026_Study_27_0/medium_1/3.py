def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[2]] == li[li[3]]

def sol():
    li = [1, 2, 3, 4]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

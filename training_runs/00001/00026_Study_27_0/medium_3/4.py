def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    li = [1, 2, 3]
    li[li[0]] = 4
    li[li[1]] = 5
    li[li[2]] = 6
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

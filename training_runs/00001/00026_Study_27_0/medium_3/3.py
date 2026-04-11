def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    li = [1, 2, 3, 4, 5]
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    li = [2, 4, 6, 8, 9, 10]
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

if __name__ == "__main__":
    assert sat(sol())

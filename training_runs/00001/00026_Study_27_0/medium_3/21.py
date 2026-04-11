def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    li = [1, 2, 3]
    while not sat(li):
        li[li[0]] = li[li[1]]
        li[li[1]] = li[li[2]]
        li[li[2]] = li[li[0]]
    return li[0]

if __name__ == "__main__":
    assert sat(sol())

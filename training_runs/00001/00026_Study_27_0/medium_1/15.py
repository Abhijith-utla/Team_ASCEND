def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[2]] == li[li[3]]

def sol():
    li = [5, 6, 7, 8]
    while not sat(li):
        li[0], li[1], li[2], li[3] = li[3], li[2], li[1], li[0]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())

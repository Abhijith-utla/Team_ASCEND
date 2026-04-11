def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[1]] == li[li[2]]

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while not sat(li):
        li = [li[i] ^ li[i+1] for i in range(0, len(li), 2)]
    return li[0]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

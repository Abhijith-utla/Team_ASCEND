def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[li[0]]] == li[li[li[1]]]

def sol():
    def check(li: List[int], idx: int):
        for i in range(len(li)):
            if li[i] == li[(idx + i) % len(li)]:
                return False
        return True

    for i in range(len(li)):
        for j in range(len(li)):
            if check(li, i * len(li) + j) and check(li, i * len(li) + j * 2) and check(li, i * len(li) + j * 3) and check(li, i * len(li) + j * 4):
                return i * len(li) + j
    return -1

print(sol())

if __name__ == "__main__":
    assert sat(sol())

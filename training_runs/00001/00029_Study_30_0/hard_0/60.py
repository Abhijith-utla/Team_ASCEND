def sat(li: List[int]):
    return all([123 * li[i] % 1000 < 123 * li[i + 1] % 1000 and li[i] in range(1000) for i in range(20)])

def sol():
    li = [i % 1000 for i in range(1000)]
    while not sat(li):
        li[0] += 1
        for i in range(1, 20):
            if li[i] >= 1000:
                li[i] = 0
                li[i - 1] += 1
    return li

def sat(li: List[int]):
    return all([123 * li[i] % 1000 < 123 * li[i + 1] % 1000 and li[i] in range(1000) for i in range(20)])

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

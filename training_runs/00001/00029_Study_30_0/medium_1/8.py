def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] >= 0 and li[i] <= 1000)) for i in range(20)])

def sol():
    li = [random.randint(-1000, 1000) for _ in range(20)]
    while not sat(li):
        li = [random.randint(-1000, 1000) for _ in range(20)]
    return li

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

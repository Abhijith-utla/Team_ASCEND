def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] >= 0) and (li[i] < 1000)) for i in range(20)])

def sol():
    li = [100, 101, 102, 123, 100, 101, 102, 123, 100, 101, 102, 123, 100, 101, 102, 123, 100, 101, 102, 123]
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

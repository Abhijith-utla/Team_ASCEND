def sat(li: List[int]):
    return all([((li[i] % 123 < 123) and (li[i] >= 0 and li[i] <= 1000)) for i in range(20)])

def sol():
    return [i for i in range(1001) if i % 123 < 123]

if __name__ == "__main__":
    assert sat(sol())

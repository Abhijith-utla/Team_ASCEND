def sat(li: List[int]):
    return all([((li[i] % 2 == 0 and li[i] % 123 == 0) and ((li[i] >= 0 and li[i] <= 1000))) for i in range(20)])

def sol():
    return [i for i in range(1000) if i % 2 == 0 and i % 123 == 0 and 0 <= i <= 1000]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

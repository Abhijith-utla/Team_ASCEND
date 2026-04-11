def sat(li: List[int]):
    return all([((li[i] % 2 == 0 and li[i] % 123 == 0) and ((li[i] >= 0 and li[i] <= 1000))) for i in range(20)])

def sol():
    return [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

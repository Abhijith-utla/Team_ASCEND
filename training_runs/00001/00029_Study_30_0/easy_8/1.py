def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and ((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] >= 0 and li[i] < 1000))) for i in range(20)])

def sol():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] >= 0 and li[i] < 1000)) for i in range(20)])

def sol():
    return [i for i in range(1000) if (123 * i % 1000 < 123 * (i + 1) % 1000) and (i >= 0 and i < 1000)]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

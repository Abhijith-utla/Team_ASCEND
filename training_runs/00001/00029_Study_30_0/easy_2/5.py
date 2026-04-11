def sat(li: List[int]):
    return all([((li[i] % 2 == 0 and li[i] % 123 == 0) and ((li[i] >= 0 and li[i] <= 1000))) for i in range(20)])

def sol():
    li = [i % 2 for i in range(1000)]
    li = [i * 123 for i in li]
    li = [i + 100 for i in li]
    li = [i for i in li if i >= 0 and i <= 1000]
    return li

# Testing
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

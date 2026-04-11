def sat(li: List[int]):
    return all([((li[i] % 2 == 0 and li[i] % 123 == 0) and ((li[i] >= 0 and li[i] <= 1000))) for i in range(20)])

def sol():
    li = [i for i in range(20) if i % 2 == 0 and i % 123 == 0 and (i >= 0 and i <= 1000)]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())

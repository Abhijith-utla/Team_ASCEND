def sat(li: List[int]):
    return all([((li[i] % 123 < 123) and (li[i] >= 0 and li[i] <= 1000)) for i in range(20)])

def sol():
    li = [0]*20
    return li

if __name__ == "__main__":
    assert sat(sol())

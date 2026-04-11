def sat(li: List[int]):
    return all([(li[i] % 2 == 0 and li[i] % 123 == 0) for i in range(20)])

def sol():
    li = [i for i in range(20)]
    return sat(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())

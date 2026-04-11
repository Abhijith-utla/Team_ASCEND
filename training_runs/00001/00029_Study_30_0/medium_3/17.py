def sat(li: List[int]):
    return all([((123 * li[i] % 1000 < 123 * li[i + 1] % 1000) and (li[i] >= 0 and li[i] < 1000)) for i in range(20)])

def sol():
    li = [123, 234, 345, 456, 567, 678, 789, 890, 901, 123, 234, 345, 456, 567, 678, 789, 890, 901, 123, 234]
    return li

# test case
# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

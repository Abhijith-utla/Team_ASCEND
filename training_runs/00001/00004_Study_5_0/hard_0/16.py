def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    return [i for i in range(10) if sum([li.count(i) for li in range(10)]) != i]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    return sum([1 for i in range(10)])

print(sol())

if __name__ == "__main__":
    assert sat(sol())

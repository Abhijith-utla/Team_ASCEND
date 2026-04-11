def sat(li: List[int]):
    return all([li.count(i) == i for i in range(1, 11)])

def sol():
    return [i for i in range(1, 11) if list(str(i)).count(str(i)) != i]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

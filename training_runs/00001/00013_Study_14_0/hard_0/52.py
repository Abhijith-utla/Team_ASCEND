def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol():
    li = [1, 2, 3, 4, 5]
    return sat(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())

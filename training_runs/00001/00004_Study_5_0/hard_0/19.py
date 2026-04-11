def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return li

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

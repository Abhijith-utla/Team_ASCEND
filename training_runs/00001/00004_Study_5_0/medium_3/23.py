def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)]) and li.count(0) == 1

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 0][::-1]

print(sol())

if __name__ == "__main__":
    assert sat(sol())

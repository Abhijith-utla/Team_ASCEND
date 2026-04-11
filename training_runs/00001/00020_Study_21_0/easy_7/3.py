def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(7)])

def sol():
    li = [1, 2, 2, 3, 3, 4, 5]
    return sat(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())

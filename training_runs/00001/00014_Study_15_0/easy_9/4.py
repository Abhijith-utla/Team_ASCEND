def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

def sol():
    li = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    return sat(li)

def sat(li: List[int]):
    return all(x == sum(li[:i]) for i in range(1, len(li) + 1))

print(sat(li))

if __name__ == "__main__":
    assert sat(sol())

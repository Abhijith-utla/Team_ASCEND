def sat(li: List[int]):
    return all(j in {i} for i, j in enumerate(li))

def sol():
    li = [1, 2, 3, 4, 5]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())

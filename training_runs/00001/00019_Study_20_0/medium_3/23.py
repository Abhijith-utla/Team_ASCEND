def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    li = [3, 6, 9]
    return sat(li)

if __name__ == "__main__":
    assert sat(sol())

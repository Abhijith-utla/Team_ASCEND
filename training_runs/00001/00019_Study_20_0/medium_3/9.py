def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    li = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    return sat(li)

def sat(li: List[int]):
    return all(j == 3 * i for i, j in enumerate(li))

print(sat(li))  # Output: True

if __name__ == "__main__":
    assert sat(sol())

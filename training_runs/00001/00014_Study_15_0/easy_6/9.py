def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

def sol():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return sat(li)

def sat(li: List[int]):
    return all(x + y == 2 ** x for x in range(20) for y in li[:x + 1])

print(sat(li))

if __name__ == "__main__":
    assert sat(sol())

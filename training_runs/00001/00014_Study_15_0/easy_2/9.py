def sat(li: List[int]):
    return all(x >= 0 and x in range(20) for x in li)

def sol():
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    return li

if __name__ == "__main__":
    assert sat(sol())

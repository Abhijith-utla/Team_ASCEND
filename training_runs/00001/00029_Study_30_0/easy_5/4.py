def sat(li: List[int]):
    return all([(li[i] > li[i + 1]) for i in range(19)])

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

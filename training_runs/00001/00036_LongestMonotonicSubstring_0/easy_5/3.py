def sat(x: List[int], length=13):
    return len(x) >= length

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if __name__ == "__main__":
    assert sat(sol())

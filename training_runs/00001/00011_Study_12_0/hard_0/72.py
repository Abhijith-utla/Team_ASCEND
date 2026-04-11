def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [i+j for i, j in zip([4] + [0]*998, [0]*999 + [4])]

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

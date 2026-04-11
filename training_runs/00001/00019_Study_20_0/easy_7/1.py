def sat(li: List[int]) -> bool:
    return all(j == 3 * i for i, j in enumerate(li))

def sol():
    li = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    return sat(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())

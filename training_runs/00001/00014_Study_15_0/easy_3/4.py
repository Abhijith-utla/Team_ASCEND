def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

def sol():
    return sat([i for i in range(1, 10)])

def sat(li: List[int]):
    return all(x >= 0 and 2 ** x - 1 == (2 ** (x + 1)) - 1 for x in li)

print(sat([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sat([2, 4, 8, 16, 32, 64, 128, 256, 512]))
print(sat([3, 6, 9, 12, 18, 27, 34, 45, 56]))
print(sat([1, 3, 5, 8, 13, 21, 34, 55, 89]))
print(sat([4, 10, 18, 30, 60, 120, 240, 480, 960]))

if __name__ == "__main__":
    assert sat(sol())

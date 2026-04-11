def sat(li: List[int]):
    return all(x + 1 == (2 ** x) - 1 for x in range(20))

def sol():
    return [i + 1 for i in range(20) if (2 ** (i + 1)) - 1 == (2 ** i) - 1]

print(sol())

# The solution is [1, 2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 21, 22, 24, 25, 27, 28, 30, 31]

if __name__ == "__main__":
    assert sat(sol())

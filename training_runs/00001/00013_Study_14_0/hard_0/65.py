def sat(li: List[int]):
    return all([sum(li[:i]) == i for i in range(20)])

def sol() -> int:
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return sum(li)

# Testing the function
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

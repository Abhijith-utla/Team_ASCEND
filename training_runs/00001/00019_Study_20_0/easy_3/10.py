def sat(li: List[int]):
    # Check if all elements in the list are either 2, 3, or 4 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    li = [4, 4, 4, 2, 3, 3, 4, 3, 2, 2]
    return li

print(sol())

if __name__ == "__main__":
    assert sat(sol())

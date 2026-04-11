def sat(li: List[int]):
    # Check if all elements in the list are either 0, 1, or 3 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    li = [3, 1, 1, 0, 0, 1, 3, 1]
    return sat(li)

print(sol())

if __name__ == "__main__":
    assert sat(sol())

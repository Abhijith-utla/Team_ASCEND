def sat(li: List[int]):
    # Check if all elements in the list are either 1, 2, or 3 times their position
    return all(j in {i - 1, i + 1, 3 * i} for i, j in enumerate(li, start=1))

def sol():
    li = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    if sat(li):
        return "valid"
    else:
        return "invalid"

print(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([5] + li, li)) and len(li) == 1000

def sol():
    return [5] + [i + 1 for i in range(999)]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

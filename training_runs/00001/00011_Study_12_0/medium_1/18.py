def sat(li: List[int]):
    return all(i + j == 1 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return 5

# The answer is 5, and it should be checked by the assert statement.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

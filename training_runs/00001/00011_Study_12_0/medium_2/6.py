def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return 2

# This assertion checks the correctness of the solution.
# It should return 2 for the given input.
assert sat(sol()) == 2

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all((j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128])))

def sol():
    return 0

# The function sat is already defined by the user. Here is the solution for the problem
def sol():
    return 0

if __name__ == "__main__":
    assert sat(sol())

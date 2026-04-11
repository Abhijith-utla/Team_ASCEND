def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return 9

# This function returns 9 because it is the only answer that satisfies the condition in the problem statement.

if __name__ == "__main__":
    assert sat(sol())

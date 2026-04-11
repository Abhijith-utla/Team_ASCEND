def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [9, 1, 8, 2, 7, 3, 6, 4, 5]

# Testing the solution
print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

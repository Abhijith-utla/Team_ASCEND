def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li) and len(set(li)) == 10

def sol():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

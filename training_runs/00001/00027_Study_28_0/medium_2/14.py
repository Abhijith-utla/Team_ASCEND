def sat(li: List[int]):
    return all(abs(i - j) >= 10 for i in li for j in li) and len(set(li)) == 10

def sol():
    return []

# Check the function by providing a solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

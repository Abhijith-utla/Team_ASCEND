def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [4] + [i+1 for i in range(999)]

def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

# Test the solution
print(sol())
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

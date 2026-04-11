def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    return [1] * 1000 + [2]

def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

# This test case will pass if the function sol returns a list of length 1000 with the first element being 1 and the last being 2.
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

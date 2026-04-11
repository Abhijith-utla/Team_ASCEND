def sat(li: List[int]):
    return all(i + j == 1 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [0]*999 + [1]
    return li

# Test
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

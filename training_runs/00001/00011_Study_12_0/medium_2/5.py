def sat(li: List[int]):
    return all(i + j == 2 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li: List[int] = [4] + [0] * 999
    return li

# Test
print(sat(sol()))  # This should print: [4, 0, 0, 0, 0, ..., 0, 0, 0]

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4]
    for _ in range(989):
        li.append(sum(li[-2:]) % 10)
    return li

print(sat(sol()))  # Expected: True

def sat(li: List[int]):
    return all(i + j == 9 for i, j in zip([4] + li, li)) and len(li) == 1000

print(sat(sol()))  # Expected: False

if __name__ == "__main__":
    assert sat(sol())

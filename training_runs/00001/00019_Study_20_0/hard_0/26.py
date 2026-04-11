def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return [1, 2, 3, 4, 5][::-1]

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

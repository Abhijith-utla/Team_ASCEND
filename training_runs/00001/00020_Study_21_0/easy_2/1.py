def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

# test case
print(sat(sol()))  # should return True

# another test case
print(sat([1, 1, 1, 2, 3, 4, 5, 6, 7]))  # should return False

# another test case
print(sat([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # should return True

if __name__ == "__main__":
    assert sat(sol())

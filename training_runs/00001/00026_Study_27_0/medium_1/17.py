def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[2]] == li[li[3]]

def sol():
    return [1, 2, 3, 4]

print(sat(sol()))  # False

# Explanation:
# The list is [1, 2, 3, 4], and we have:
# li[0] = li[1] = li[2] = li[3] = 1, 2, 3, 4
# li[0] != li[1] = True, li[2] == li[3] = True
# Therefore, the function returns False.

if __name__ == "__main__":
    assert sat(sol())

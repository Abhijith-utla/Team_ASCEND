def sat(li: List[int]):
    return all([li[i] != li[i + 2] for i in range(len(li) - 1)]) and len(set(li)) == 3

def sol():
    return [1, 2, 3]

# The function 'sat' checks if all elements in the list are different from the next one and the list contains exactly 3 unique elements.
# The list [1, 2, 3] satisfies all these conditions.

if __name__ == "__main__":
    assert sat(sol())

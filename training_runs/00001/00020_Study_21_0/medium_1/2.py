def sat(li: List[int]):
    return all([li[i] != li[i + 1] for i in range(9)]) and len(set(li)) == 3

def sol():
    return []

# The function sat checks whether the list li contains unique elements and no two consecutive elements are the same. 
# The checker will run: assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

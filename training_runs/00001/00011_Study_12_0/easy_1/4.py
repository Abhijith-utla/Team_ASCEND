def sat(li: List[int]):
    return all(i + j == 1 for i, j in zip([4] + li, li)) and len(li) == 1000

def sol():
    li = [4] + [0]*998
    return li

# This will make sure the function sat(li) returns a list of length 1000 and all elements are equal to 4
assert sat(li)

if __name__ == "__main__":
    assert sat(sol())

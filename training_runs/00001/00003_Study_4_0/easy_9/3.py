def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    if li.index(li[3]) != 4:
        return False
    return True

def sol():
    li = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5]
    return li

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

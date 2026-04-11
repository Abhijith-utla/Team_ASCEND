def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    if li.index(li[3]) != 3:
        return False
    if li.count(li[3]) != 1:
        return False
    return True

def sol():
    li = [1, 1, 2, 4, 4, 4, 7, 7, 8, 10]
    return li

# Testing the solution
assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    if li.index(li[3]) == 3:
        return False
    if li.count(li[3]) != 1:
        return False
    return True

def sol():
    li = [1, 2, 3, 3, 2, 1, 4, 5, 5, 6]
    return li

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

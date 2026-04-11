def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    if li.index(li[3]) != 3:
        return False
    if li.count(li[3]) == 1:
        return False
    return True

def sol():
    li = [0] * 10
    li[3] = 1
    li[4] = 1
    li[5] = 1
    li[6] = 1
    li[7] = 1
    li[8] = 1
    li[9] = 1
    return li

print(sat(sol()))

if __name__ == "__main__":
    assert sat(sol())

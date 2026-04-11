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
    li = [0]*10
    li[3] = 1
    li[4] = 2
    li[5] = 3
    li[7] = 4
    li[8] = 5
    li[9] = 6
    li[2] = 7
    li[6] = 8
    li[1] = 9
    return li

assert sat(sol())

if __name__ == "__main__":
    assert sat(sol())

def sat(li: List[int]) -> bool:
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    return True

def sol():
    li = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
    if len(li) != 10:
        return False
    if li.count(li[3]) != 2:
        return False
    return True

print(sat(li))

if __name__ == "__main__":
    assert sat(sol())

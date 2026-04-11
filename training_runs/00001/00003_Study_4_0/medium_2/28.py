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

def sol() -> bool:
    li: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return sat(li)

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

# Test the solution
print(sol())

if __name__ == "__main__":
    assert sat(sol())
